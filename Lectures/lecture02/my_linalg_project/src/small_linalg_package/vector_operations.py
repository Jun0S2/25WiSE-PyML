import numpy as np
from typing import List


def inner_product(vector1: np.array, vector2: np.array) -> np.array:
    """
    Compute the inner product of two vectors.

    Parameters:
    vector1 (np.array): The first vector.
    vector2 (np.array): The second vector.

    Returns:
    np.array: The inner product of the two vectors.

    Raises:
    ValueError: If the shape of the two vectors is not the same. 
    """
    if vector1.shape != vector2.shape:
        raise ValueError("vectors must have the same dimensions")

    return vector1 @ vector2


def elementwise_add(vector1: np.array, vector2: np.array) -> np.array:
    """
    Compute the element-wise addition of two vectors.

    Parameters:
    vector1 (np.array): The first vector.
    vector2 (np.array): The second vector.

    Returns:
    np.array: The result of element-wise addition.

    Raises:
    ValueError: If the vectors do not have the same dimensions.
    """
    if vector1.shape != vector2.shape:
        raise ValueError("vectors must have the same dimensions")
    
    return vector1 + vector2


def elementwise_multiply(vector1: np.array, vector2: np.array) -> np.array:
    """
    Compute the element-wise multiplication of two vectors.

    Parameters:
    vector1 (np.array): The first vector.
    vector2 (np.array): The second vector.

    Returns:
    np.array: The result of element-wise multiplication.

    Raises:
    ValueError: If the vectors do not have the same dimensions.
    """
    if vector1.shape != vector2.shape:
        raise ValueError("vectors must have the same dimensions")
    
    return vector1 * vector2
