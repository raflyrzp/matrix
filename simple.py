def input_matrix(rows, cols, name):
    matrix = []
    print(f"\nEnter elements for Matrix {name}:")
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)
    return matrix

def multiply_matrix(a, b):
    if len(a[0]) != len(b):
        print("Cannot multiply Matrix A and Matrix B. The number of columns in Matrix A must be equal to the number of rows in Matrix B.")
        return None

    result = []
    for i in range(len(a)):
        result.append([])
        for j in range(len(b[0])):
            cell_value = 0
            for k in range(len(b)):
                cell_value += a[i][k] * b[k][j]
            result[i].append(cell_value)
    return result

def print_matrix(matrix, name=""):
    if name:
        print(f"\n{name} :")
    for row in matrix:
        print(f"[{' '.join(map(str, row))}]")

if __name__ == "__main__":
    rows_a = int(input("Enter the number of rows for Matrix A: "))
    cols_a = int(input("Enter the number of columns for Matrix A: "))
    matrix_a = input_matrix(rows_a, cols_a, "A")

    rows_b = int(input("Enter the number of rows for Matrix B: "))
    cols_b = int(input("Enter the number of columns for Matrix B: "))
    matrix_b = input_matrix(rows_b, cols_b, "B")

    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")

    multiplication_result = multiply_matrix(matrix_a, matrix_b)

    if multiplication_result:
        print_matrix(multiplication_result, "Result of Matrix A and B Multiplication")