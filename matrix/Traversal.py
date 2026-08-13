# In here we will find the traversal techniques
# row-wise
def row_wise(matrix):
    result = []
    for row in matrix:
        result.extend(row)
    return result

# column-wise
def column_wise(matrix):
    result = []
    rows, columns = len(matrix), len(matrix[0])
    for j in range(columns):
        for i in range(rows):
            result.append(matrix[i][j])
    return result

array = [ [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9] 
    ]
print(row_wise(array))
print(column_wise(array))


def rowWise(matrix):
    result = []
    for row in matrix:
        result.extend(row)
    return result

print(rowWise(array))

def columnWise(matrix):
    result = []
    rows, columns = len(matrix), len(matrix[0])
    for j in range(columns):
        for i in range(rows):
            result.append(matrix[i][j])
    return result

print(columnWise(array))