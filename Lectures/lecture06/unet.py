import torch
import torch.nn as nn
import torch.nn.functional as F
import math


class SinusoidalPositionEmbeddings(nn.Module):
    """Sinusoidal position embeddings for time"""
    def __init__(self, dim):
        super().__init__()
        self.dim = dim

    def forward(self, time):
        device = time.device
        half_dim = self.dim // 2
        embeddings = math.log(10000) / (half_dim - 1)
        embeddings = torch.exp(torch.arange(half_dim, device=device) * -embeddings)
        embeddings = time[:, None] * embeddings[None, :]
        embeddings = torch.cat((embeddings.sin(), embeddings.cos()), dim=-1)
        return embeddings


class DownBlock(nn.Module):
    """Downsampling block with time embedding"""
    def __init__(self, in_ch, out_ch, time_emb_dim):
        super().__init__()
        self.time_mlp = nn.Linear(time_emb_dim, out_ch)
        
        self.conv1 = nn.Conv2d(in_ch, out_ch, 3, padding=1)
        self.conv2 = nn.Conv2d(out_ch, out_ch, 3, padding=1)
        self.bnorm1 = nn.BatchNorm2d(out_ch)
        self.bnorm2 = nn.BatchNorm2d(out_ch)
        self.relu = nn.ReLU()
        self.downsample = nn.Conv2d(out_ch, out_ch, 4, 2, 1)
        
    def forward(self, x, t):
        # First conv
        h = self.bnorm1(self.relu(self.conv1(x)))
        # Time embedding
        time_emb = self.relu(self.time_mlp(t))
        # Extend time embeddings to [b, c, h, w]
        time_emb = time_emb[(..., ) + (None, ) * 2]
        # Add time embeddings
        h = h + time_emb
        # Second conv
        h = self.bnorm2(self.relu(self.conv2(h)))
        # Downsample
        return self.downsample(h)


class UpBlock(nn.Module):
    """Upsampling block with skip connection and time embedding"""
    def __init__(self, in_ch, out_ch, time_emb_dim):
        super().__init__()
        self.time_mlp = nn.Linear(time_emb_dim, out_ch)
        
        self.upsample = nn.ConvTranspose2d(in_ch, in_ch, 4, 2, 1)
        self.conv1 = nn.Conv2d(in_ch + in_ch//2, out_ch, 3, padding=1)  # + skip connection
        self.conv2 = nn.Conv2d(out_ch, out_ch, 3, padding=1)
        self.bnorm1 = nn.BatchNorm2d(out_ch)
        self.bnorm2 = nn.BatchNorm2d(out_ch)
        self.relu = nn.ReLU()
        
    def forward(self, x, skip, t):
        # Upsample
        x = self.upsample(x)
        # Crop or pad x to match skip's spatial size
        diffY = skip.size(2) - x.size(2)
        diffX = skip.size(3) - x.size(3)
        if diffY != 0 or diffX != 0:
            x = F.pad(x, [diffX // 2, diffX - diffX // 2, diffY // 2, diffY - diffY // 2])
        # Concatenate with skip connection
        x = torch.cat([x, skip], dim=1)
        # First conv
        h = self.bnorm1(self.relu(self.conv1(x)))
        # Time embedding
        time_emb = self.relu(self.time_mlp(t))
        # Extend time embeddings to [b, c, h, w]
        time_emb = time_emb[(..., ) + (None, ) * 2]
        # Add time embeddings
        h = h + time_emb
        # Second conv
        h = self.bnorm2(self.relu(self.conv2(h)))
        return h


class SimpleUNet(nn.Module):
    """Simple UNet for diffusion models (high capacity)"""
    def __init__(self, in_channels=1, out_channels=1, time_dim=256, device="cpu"):
        super().__init__()
        self.device = device
        self.time_dim = time_dim
        
        # Time embeddings
        self.time_mlp = nn.Sequential(
            SinusoidalPositionEmbeddings(time_dim),
            nn.Linear(time_dim, time_dim),
            nn.ReLU()
        )
        
        # Initial projection
        self.conv0 = nn.Conv2d(in_channels, 128, 3, padding=1)
        
        # Downsampling
        self.down1 = DownBlock(128, 256, time_dim)
        self.down2 = DownBlock(256, 512, time_dim)
        self.down3 = DownBlock(512, 1024, time_dim)
        
        # Bottleneck
        self.bottleneck = nn.Sequential(
            nn.Conv2d(1024, 1024, 3, padding=1),
            nn.BatchNorm2d(1024),
            nn.ReLU(),
            nn.Conv2d(1024, 1024, 3, padding=1),
            nn.BatchNorm2d(1024),
            nn.ReLU(),
        )
        
        # Upsampling
        self.up1 = UpBlock(1024, 512, time_dim)
        self.up2 = UpBlock(512, 256, time_dim)
        self.up3 = UpBlock(256, 128, time_dim)
        
        # Output
        self.output = nn.Conv2d(128, out_channels, 1)
        
    def forward(self, x, t):
        """
        Args:
            x: Input image tensor [B, C, H, W]
            t: Time tensor [B]
        Returns:
            Predicted noise [B, C, H, W]
        """
        # Time embeddings
        t = self.time_mlp(t)
        
        # Initial conv
        x0 = self.conv0(x)
        
        # Downsampling with skip connections
        x1 = self.down1(x0, t)
        x2 = self.down2(x1, t)
        x3 = self.down3(x2, t)
        
        # Bottleneck
        x3 = self.bottleneck(x3)
        
        # Upsampling with skip connections
        x = self.up1(x3, x2, t)
        x = self.up2(x, x1, t)
        x = self.up3(x, x0, t)
        
        # Output
        return self.output(x)


if __name__ == "__main__":
    # Device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Initialize the UNet
    model = SimpleUNet(in_channels=1, out_channels=1, time_dim=256, device=str(device)).to(device)

    # Create input tensors
    x = torch.randn(64, 1, 14, 14).to(device)  # Batch of 64 images
    t = torch.randint(0, 1000, (64,)).to(device)  # Batch of 64 time steps

    # Forward pass
    with torch.no_grad():
        output = model(x, t)

    print(f"Input shape: {x.shape}")
    print(f"Time shape: {t.shape}")
    print(f"Output shape: {output.shape}")