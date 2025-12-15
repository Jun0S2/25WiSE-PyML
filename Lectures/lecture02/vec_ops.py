# vector_operations.py
import numpy as np 

def _shape_check(vector1:np.array, vector2:np.array) -> None:
    if vector1.shape != vector2.shape:
        raise ValueError("Vectors must have the same shape")


def inner_product(vector1:np.array, vector2:np.array) -> float:
    _shape_check(vector1, vector2)
    return vector1 @ vector2


def elementwise_add(vector1:np.array, vector2:np.array) -> np.array:
    _shape_check(vector1, vector2)
    return vector1 + vector2


def elementwise_multiply(vector1:np.array, vector2:np.array) -> np.array:
    _shape_check(vector1, vector2)
    return vector1 * vector2