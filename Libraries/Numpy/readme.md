# NumPy Basics — Study Summary

**Resource:** [W3Schools NumPy](https://www.w3schools.com/python/numpy/numpy_array_filter.asp)  
**File link:** [./0_intro.ipynb](./0_intro.ipynb)

---

## 1. NumPy Intro

- NumPy is a Python library for numerical computing.
- It provides support for large, multi-dimensional arrays and matrices.
- Offers a variety of mathematical functions to operate on these arrays efficiently.

---

## 2. NumPy Getting Started

- Install with `pip install numpy`.
- Import using `import numpy as np`.
- NumPy arrays are called `ndarray` (n-dimensional array).
- Arrays are faster and more memory-efficient than Python lists.

---

## 3. NumPy Creating Arrays

- Create from Python lists: `np.array([1, 2, 3])`
- Functions for arrays:
  - `np.zeros((2,3))` — array of zeros
  - `np.ones((2,3))` — array of ones
  - `np.arange(start, stop, step)` — like Python range
  - `np.linspace(start, stop, num)` — evenly spaced numbers
  - `np.random.random((2,3))` — random numbers

---

## 4. NumPy Array Indexing

- Access elements by index: `arr[0]`, `arr[1,2]`
- Supports negative indexing: `arr[-1]` returns the last element
- Indexing is zero-based

---

## 5. NumPy Array Slicing

- Syntax: `arr[start:stop:step]`
- Multi-dimensional slicing: `arr[0:2, 1:3]`
- Creates a **view**, not a copy (changes affect original array)

---

## 6. NumPy Data Types

- Each array has a `dtype` attribute.
- Common types: `int32`, `float64`, `bool`
- Can specify type during creation: `np.array([1,2,3], dtype=float)`

---

## 7. NumPy Copy vs View

- **View**: points to the same data, changes affect original array.
- **Copy**: independent copy, changes do not affect original array.
- Use `arr.copy()` to make a copy.

---

## 8. NumPy Array Shape

- `arr.shape` gives dimensions (rows, columns)
- `arr.ndim` gives number of dimensions
- `arr.size` gives total number of elements

---

## 9. NumPy Array Reshape

- Change shape without changing data: `arr.reshape((new_rows, new_cols))`
- `-1` can be used to infer dimension automatically: `arr.reshape(-1, 2)`

---

## 10. NumPy Array Iterating

- Iterate using for-loops: `for x in arr:`
- Use `np.nditer(arr)` for multi-dimensional arrays
- Efficient iteration avoids creating temporary arrays

---

## 11. NumPy Array Join

- Concatenate arrays: `np.concatenate([arr1, arr2])`
- Stack vertically: `np.vstack([arr1, arr2])`
- Stack horizontally: `np.hstack([arr1, arr2])`

---

## 12. NumPy Array Split

- Split arrays: `np.array_split(arr, 3)` divides into 3 parts
- `np.hsplit(arr, 2)` — horizontal split
- `np.vsplit(arr, 2)` — vertical split

---

## 13. NumPy Array Search

- Find elements: `np.where(arr > 5)`
- Check existence: `5 in arr`
- Get index of max/min: `arr.argmax()`, `arr.argmin()`

---

## 14. NumPy Array Sort

- Sort array: `np.sort(arr)`
- Sort in-place: `arr.sort()`
- Sorting along axis: `np.sort(arr, axis=0)` (columns), `axis=1` (rows)

---

## 15. NumPy Array Filter

- Filter elements using conditions: `arr[arr > 5]`
- Can combine conditions: `arr[(arr > 2) & (arr < 8)]`
- Boolean indexing creates a new array with selected elements

---

**End of NumPy Basics Summary**
