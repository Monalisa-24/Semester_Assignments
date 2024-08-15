def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise ValueError("Both matrices must have the same dimensions.")
    result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[i]))] for i in range(len(matrix1))]
    return result
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
try:
    print("Enter the first matrix row by row (separate elements by spaces, rows by new lines). Type 'done' when finished:")
    matrix1 = []
    while True:
        row = input()
        if row.lower() == 'done':
            break
        matrix1.append(list(map(int, row.split())))
    print("Enter the second matrix row by row (separate elements by spaces, rows by new lines). Type 'done' when finished:")
    matrix2 = []
    while True:
        row = input()
        if row.lower() == 'done':
            break
        matrix2.append(list(map(int, row.split())))
    result = subtract_matrices(matrix1, matrix2)
    print("Result of matrix subtraction:")
    print_matrix(result)
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
