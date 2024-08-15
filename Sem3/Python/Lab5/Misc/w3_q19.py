def multiply_matrices(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    if cols1 != rows2:
        raise ValueError("Number of columns in the first matrix must be equal to number of rows in the second matrix.")
    result = [[0] * cols2 for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
def get_matrix_input(prompt):
    print(prompt)
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    matrix = []
    for _ in range(rows):
        row = list(map(int, input(f"Enter row values separated by spaces: ").split()))
        if len(row) != cols:
            raise ValueError("Row length does not match the specified number of columns.")
        matrix.append(row)
    return matrix
matrix1 = get_matrix_input("Enter the first matrix:")
matrix2 = get_matrix_input("Enter the second matrix:")
try:
    result_matrix = multiply_matrices(matrix1, matrix2)
    print("The resulting matrix after multiplication is:")
    for row in result_matrix:
        print(' '.join(map(str, row)))
except ValueError as e:
    print(e)
