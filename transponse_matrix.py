# we will try to transpose a matrix
import numpy as np

def transpose(arr):
    rows = len(arr)
    columns = len(arr[0]) if rows > 0 else 0

    return_arr = [[0]*rows for _ in range(columns)]

    for i in range(rows):
        for j in range(columns):
            return_arr[i][j]= arr[j][i]
    
    return return_arr




arr =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(transpose(arr))

arr1 = arr.copy()
arr = np.array(arr)
print("Trasposed matrix using numpy: \n", arr.T)


def tranposeMatrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0]) if rows > 0 else 0 

    arr = [[0]*rows for _ in range(columns)]

    for i in range(rows):
        for j in range(columns):
            arr[i][j] = matrix[j][i]
    return arr

# print
print("Trasposed matrix using numpy: \n", tranposeMatrix(arr1))
