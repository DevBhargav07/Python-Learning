# we will try to write all the flipping Matrix in here.
# import os
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent

# os.path.join(BASE_DIR)
# from matrix.transpose_matrix import transpose
# from typing import list

MATRIX = list[list]

def transpose_matrix(matrix: MATRIX):
    rows = len(matrix)
    columns = len(matrix[0]) if rows > 0 else 0

    res_matrix = [[0]*rows for _ in range(columns)]

    for i in range(rows):
        for j in range(columns):
            res_matrix[j][i] = matrix[i][j]
    return res_matrix

def flip_horizontal(matrix: MATRIX) -> MATRIX:
    return [row[::-1] for row in matrix]

def flip_vertical(matrix: MATRIX) -> MATRIX:
    return matrix[::-1]

def rotate_90_deg(matrix: MATRIX, clock_wise=True, transpose=True) -> MATRIX:
    # to get the 90_deg rotation
    # call the transpose & horizontal flipping
    # if clock_wise = True
    if transpose:
        matrix = transpose_matrix(matrix)
    
    if clock_wise:
        return flip_horizontal(matrix)
    # if not a clockwise then it is calledd for anti-clockwise
    return flip_vertical(matrix)

def rotate_180_deg(matrix: MATRIX) -> MATRIX:
    # for both clockwise and anti-clockwise both are having the same process we will
    # do the clockwise
    # first call horizontal & then vertical
    return flip_vertical(flip_horizontal(matrix))

def print_arr(arr: MATRIX) -> list:
    for ar in arr:
        print(ar)

# arr = [[1,2,3],[4,5,6],[7,8,9]]
arr = [[0,1,3],[9,5,8]]
print("Before rotating/flipping")
print_arr(arr)
result = flip_horizontal(arr)
print("After flipping")
print_arr(result)
print("After rotating vertically")
res = flip_vertical(arr)
print_arr(res)
print("rotating 90 degrees - clock wise")
res = rotate_90_deg(arr, clock_wise=True)
print_arr(res)
print("rotating 90 degrees - Anticlock wise")
res = rotate_90_deg(arr, clock_wise=False)
print_arr(res)
print("rotating 180 degrees - clock/Anticlock wise")
res = rotate_180_deg(arr)
print_arr(res)
print("rotating 270 degrees - clock wise")
res = rotate_90_deg(arr, clock_wise=False, transpose=False)
print_arr(res)

print("rotating 270 degrees - Anticlock wise")
res = rotate_90_deg(arr, clock_wise=True, transpose=False)
print_arr(res)
