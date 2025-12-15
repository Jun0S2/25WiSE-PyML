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



if __name__=="__main__":
    import sys 

    if len(sys.argv) != 3:
        print("Usage: python script.py vector1 vector2")
        sys.exit(1)

    try:
        vector1 = np.array([float(x) for x in sys.argv[1].split(',')])
        vector2 = np.array([float(x) for x in sys.argv[2].split(',')])
    except ValueError:
        print("Vectors must contain only numerical values separated by commas")
        sys.exit(1)

    print("Vector 1:", vector1)
    print("Vector 2:", vector2)

    print("Inner Product:", inner_product(vector1, vector2))
    print("Elementwise Addition:", elementwise_add(vector1, vector2))
    print("Elementwise Multiplication:", elementwise_multiply(vector1, vector2))

