# we will learn about the matrix
# diagnal printing values
import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Our matrix using numpy")
print(array)

print("Element at [0][0]", array[0,0])

# getting the entire first row
print("Elements at [0]", array[0,:])

# getting the entire last column
print("Elements at [2]", array[:, 2])


# creating a matrix with all zeros
zeros_matrix = np.zeros((2,4))
print(zeros_matrix)

# creating random 3x3 matrix using the random numbers between 0 and 1
random_matrix = np.random.rand(3,3)
print(random_matrix)



# test
game_map = np.array([
    [0, 0, 0, 0],
    [0, 0, 9, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 9]
])

# finding the first 9
print(game_map[1][2])


# printing the entire fourth column
print("Entire 4th column is: ", game_map[:, 3])
# print("Entire 5th column is: ", game_map[:, 4])


# MATRIX OPERATIONS & DIAGONALS

# 1.Extracting the diagonal
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print('Diagonal values are: ', np.diag(matrix))

#2. Flipping the matrix (The Transpose)
transposed_matrix = matrix.T
print("Original Matrix\n", matrix)
print("Transposed matrix:\n ", transposed_matrix)


# doubling every element in matrix
doubled = matrix * 2
print("Doubled matrix is:\n ", doubled)


# test-2
# import numpy as np

system_matrix = np.array([
    [1,  2,  3],
    [10, 20, 30],
    [100, 200, 300]
])

"""
Step 1: Create a new matrix by transposing system_matrix.

Step 2: From that new transposed matrix, extract the main diagonal values.

Step 3: Multiply those extracted diagonal values by 5 and print the final result.
"""
# step1
transposing_matrix = system_matrix.T 
print("Transposing matrix is: \n", transposing_matrix)

# step2
transposed_diag = np.diag(transposing_matrix)
print("Transposing matrix diagonal values: \n", transposed_diag)

# step 3
multiplied = transposed_diag * 5
print("Final miltiplied matrix by 5: ", multiplied)



# Inversing a color - dark mode to light mode
# when we do inverse a color (mobile, laptop anything) the code wll do the following
secret_image = np.array([
    [0,   128, 255],
    [50,  100, 150],
    [200, 220, 240]
])

inverse_image = 255 - secret_image

print("Original Image Matrix: \n", secret_image)
print("Inversed Image Matrix: \n", inverse_image)

# When you hit the "Negative" or "Invert Colors" button on your phone,
# the processor runs this exact matrix subtraction on millions of pixels simultaneously 
# using hardware optimized for NumPy-like operations.
print(len(inverse_image))

rectangle_matrix = np.array([
    [0,10],
    [20,30],
    [40,50]
])

print(len(rectangle_matrix))

