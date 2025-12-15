import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np
import torch

def print_folder_structure(data_path, indent="", max_files=3, include_files=True):
    """
    Recursively print all folders and subfolders in data_path
    Shows only first 3 files per folder, then "..." if more exist
    
    Args:
        data_path (str): Path to the directory to explore
        indent (str): Indentation for nested levels
        max_files (int): Maximum number of files to show per folder
        include_files (bool): Whether to include files in the output
    """
    if not os.path.exists(data_path):
        print(f"Path {data_path} does not exist!")
        return
    
    if not os.path.isdir(data_path):
        print(f"{data_path} is not a directory!")
        return
    
    print(f"{indent}📁 {os.path.basename(data_path)}/")
    
    try:
        # Get all items in the directory
        items = os.listdir(data_path)
        
        # Separate folders and files
        folders = []
        files = []
        
        for item in items:
            item_path = os.path.join(data_path, item)
            if os.path.isdir(item_path):
                folders.append(item)
            else:
                files.append(item)
        
        # Print folders first (recursively)
        for folder in sorted(folders):
            folder_path = os.path.join(data_path, folder)
            print_folder_structure(folder_path, indent + "  ", max_files, include_files)
        
        # Print files (limited to max_files) only if include_files is True
        if include_files:
            files.sort()
            for i, file in enumerate(files):
                if i < max_files:
                    print(f"{indent}  📄 {file}")
                else:
                    print(f"{indent}  ...")
                    break
                
    except PermissionError:
        print(f"{indent}  ❌ Permission denied")
    except Exception as e:
        print(f"{indent}  ❌ Error: {e}")

def plot_mnist_images(data_path, digit, num_images=10, figsize=(20, 2)):
    """
    Plot MNIST images in a 1xN grid
    
    Args:
        data_path (str): Path to the MNIST data directory
        digit (int): The digit to plot (0-9)    
        num_images (int): Number of images to display (default: 10)
        figsize (tuple): Figure size (width, height)
    """
    # Path to the digit training set
    digit_training_path = os.path.join(data_path, f"1/trainingSet/trainingSet/{digit}")
    
    # Check if path exists
    if not os.path.exists(digit_training_path):
        print(f"Path {digit_training_path} does not exist!")
        return
    
    # Get a list of all images for this digit
    digit_images = [f for f in os.listdir(digit_training_path) if f.endswith('.jpg')]
    
    if len(digit_images) == 0:
        print(f"No images found for digit {digit}")
        return
    
    # Select images to display
    selected_images = digit_images[:num_images]
    
    # Create a 1xN subplot grid
    fig, axes = plt.subplots(1, num_images, figsize=figsize)
    
    # Handle case where there's only one image
    if num_images == 1:
        axes = [axes]
    
    for i, img_name in enumerate(selected_images):
        image_path = os.path.join(digit_training_path, img_name)
        image = Image.open(image_path)
        
        axes[i].imshow(image, cmap='gray')
        axes[i].set_title(f'{digit}: {img_name}')
        axes[i].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    print(f"Displayed {len(selected_images)} MNIST {digit} images")

def view_samples(dataset, n_samples=10, target_key='image', label_key='label'):
    # create a figure with n_samples rows and 1 column
    fig, axis = plt.subplots(nrows=1, ncols=n_samples, figsize=(10, 1))

    # randomly select n_samples from the dataset
    ids = np.random.choice(len(dataset), n_samples)

    # loop over the selected ids and plot the images
    for i, ax in zip(ids, axis.ravel()):
        # get the image and label from the dataset
        image, label = dataset[i][target_key], dataset[i]['label']

        # load the corresponding structures and plot with `imshow`
        if type(image) == torch.Tensor:
            ax.imshow(image.squeeze(), cmap='gray', interpolation="none")
        else:
            ax.imshow(image, cmap='gray', interpolation="none")

        ax.set_title(label.item(), fontsize=12)
        ax.axis(False);
    plt.show()