import numpy as np
from typing import List


def inner_product(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    """
    Compute the inner product of two matrices.

    Parameters:
    matrix1 (np.ndarray): The first matrix of dimensions n x k.
    matrix2 (np.ndarray): The second matrix of dimensions k x m.

    Returns:
    np.ndarray: The inner product of the two matrices of dimension n x m.

    Raises:
    ValueError: If the number of columns in matrix1 does not match the number of rows in matrix2. 
    """
    if matrix1.shape[1] != matrix1.shape[0]:
        raise ValueError("Number of columns in matrix1 must match number of rows in matrix2")

    return matrix1 @ matrix2


def elementwise_add(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    """
    Compute the element-wise addition of two matrices.

    Parameters:
    matrix1 (np.ndarray): The first matrix.
    matrix2 (np.ndarray): The second matrix.

    Returns:
    np.ndarray: The result of element-wise addition.

    Raises:
    ValueError: If the matrices do not have the same dimensions.
    """
    if matrix1.shape != matrix2.shape:
        raise ValueError("Matrices must have the same dimensions")
    
    return matrix1 + matrix2


def elementwise_multiply(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    """
    Compute the element-wise multiplication of two matrices.

    Parameters:
    matrix1 (np.ndarray): The first matrix.
    matrix2 (np.ndarray): The second matrix.

    Returns:
    np.ndarray: The result of element-wise multiplication.

    Raises:
    ValueError: If the matrices do not have the same dimensions.
    """
    if matrix1.shape != matrix2.shape:
        raise ValueError("Matrices must have the same dimensions")
    
    return matrix1 * matrix2


def transpose(matrix: np.ndarray) -> np.ndarray:
    """
    Compute the transpose of a matrix.

    Parameters:
    matrix (np.ndarray): The matrix.

    Returns:
    np.ndarray: The transpose of the matrix.
    """
    return np.transpose(matrix)
