# create two func ==> max_matrix, min_matrix including all elements in it's role
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


def max_matrix(matrix):
    result = []
    for row in matrix:
        row_max = row[0] # first item in the row is assumed max
        for item in row:
            if item > row_max:
                row_max = item # update max if current item is greater than max
        
        result.append(row_max)
    return result

print(max_matrix(matrix))


def min_matrix(matrix):
    result = []
    for row in matrix:
        row_min = row[0]
        for item in row:
            if item < row_min:
                row_min = item
        result.append(row_min)
    return result

print(min_matrix(matrix))


# Alternatively using max() and min()

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [45,6,77,5],
    [76,54,75,45],
    [45,2442,552,53,57]
]


def max_matrix2(matrix):
    result = []
    for row in matrix:
        result.append(max(row))
    return result

print(max_matrix2(matrix))


def min_matrix2(matrix):
    result = []
    for row in matrix:
        result.append(min(row))
    return result

print(min_matrix2(matrix))

# using list comprehension

def max_matrix3(matrix):
    return([max(row) for row in matrix])

print(max_matrix3(matrix))

def min_matrix3(matrix):
    return([min(row) for row in matrix])

print(min_matrix3(matrix))

# len_matrix ==> should tell you how many elements in a matrix, additionally should tell you the size of the matrix

def len_matrix(matrix):
    count = 0
    for row in matrix:
        for item in row:
            count += 1
    
    rows = len(matrix)
    cols = len(matrix[0])
    print(f"Total elements in matrix: {count}")
    print(f"The dimension of the matrix is {rows}x{cols}")
len_matrix(matrix)

def len_matrix_comp(matrix):
    count = sum([len(row) for row in matrix])
    rows = len(matrix)
    cols = len(matrix[0])
    print(f"comp: Total elements in matrix: {count}")
    print(f"comp: The dimension of the matrix is {rows}x{cols}")

len_matrix_comp(matrix)

# transpose_matrix ==> converting rows to column

matrix = [
    [1,2,3,6,90],
    [4,5,6,65,22],
    [7,8,9,54,64],
    [45,6,77,5,39],
    [76,54,75,45,43],
    [45,2442,552,53,57]
]
def trnaspose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)
    
    return result

print(trnaspose_matrix(matrix))

# using nested list comprehensions
print("comp transpose", end="\n")
def transpose_matrix_comp(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    return([[matrix[r][c] for c in range(cols) ] for r in range(rows)])

print(transpose_matrix_comp(matrix))












