# we will learn about the matrix multiplication
import numpy as np

A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

result = A @ B 

print(f"Matrix multiplication :\n {result} ")

X = np.array([
    [1, 2, 3],
    [4, 5, 6]
]) # Shape is 2x3 (2 rows, 3 columns)

Y = np.array([
    # [7, 8],
    # [9, 10],
    # [11, 12]
    [7,8,9,10],
    [11,12,13,14],
    [15,16,17,18]
]) # Shape is 3x2 (3 rows, 2 columns)
# Y = np.array(
#     [40],
#     [55],
#     [13]
# )

result = X @ Y
print(result)