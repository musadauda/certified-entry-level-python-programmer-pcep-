matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(f"Element at row 0, col 1: {matrix[0][1]}") # Output: 2
first_row = matrix[0]
print(first_row)

print(matrix)
print(len(matrix))


# Looping through a multi-dimensional list

# create as many nested for loops as there are multidimensional list

def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, end=" ")
        print() # gives us a new line after each inner loop

# List comprehension in multidimensional list
# [[list comprehension for row] for row in matrix]

matrix_comp = [[x*3 for x in row] for row in matrix]
print_matrix(matrix_comp)
print(matrix_comp)

# Grid

grid = [[0 for _ in range(3)] for _ in range(3)]
print(grid)

# Tuple Matrix

tuple_matrix = (
    (1,2,3),
    (4,5,6),
    (7,8,9)

)

list_tuple_matrix = [
    (1,2,3),
    (4,5,6),
    (7,8,9)
] # existing data is ummutable but you can add or delete data

tuple_list_matrix = (
    [1,2,3],
    [4,5,6],
    [7,8,9]
) # cannot add to matrix but can add or modify the inside matrix

set_matrix = {
    frozenset([3,4,5]),
    frozenset([5,7,8]),
    frozenset([5,4,1])
} #frozenset can never be changed or modify 
print(set_matrix)

print_matrix(set_matrix)
