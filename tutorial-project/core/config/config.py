from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GlobalConfig:
    # Set both paths to writable locations before running training or eval.
    dir_experiments: Path = Path("/custom-path/to/expt/results")
    dir_data: Path = Path("/custom-path/to/data")


@dataclass
class ModelConfig:
    seed: int = 42

    # Training (dummy values)
    learning_rate: float = 0.001
    batch_size: int = 32
    n_epochs: int = 10

    # Model (dummy values)
    hidden_layer_sizes: tuple[int, ...] = (128, 64, 32)
