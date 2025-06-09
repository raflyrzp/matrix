def input_matrix(rows, cols, name):
    print(f"\nEnter matrix {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Row {i+1} (enter {cols} numbers separated by spaces): ").strip()
            row_values = row_input.split()
            if len(row_values) != cols:
                print(f"Number of values must be {cols}. Please try again.")
                continue
            try:
                row = [int(x) for x in row_values]
                matrix.append(row)
                break
            except ValueError:
                print("Input must be numbers. Please try again.")
    return matrix

def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    if cols_A != rows_B:
        raise ValueError("Number of columns in Matrix A must equal number of rows in Matrix B.")
    
    result = []
    for i in range(rows_A):
        result_row = []
        for j in range(cols_B):
            total = 0
            for k in range(cols_A):
                total += A[i][k] * B[k][j]
            result_row.append(total)
        result.append(result_row)
    return result

def print_matrix(matrix, name="Matrix"):
    print(f"\n{name}:")
    for row in matrix:
        print(f"[{' '.join(str(x) for x in row)}]")

while True:
    try:
        rows_A = int(input("Enter the number of rows for Matrix A: "))
        cols_A = int(input("Enter the number of columns for Matrix A: "))
        if rows_A <= 0 or cols_A <= 0:
            print("Please enter positive integers for matrix size.")
            continue
        break
    except ValueError:
        print("Input must be an integer. Please try again.")

print(f"Matrix B must have {cols_A} rows to be compatible for multiplication.")

while True:
    try:
        rows_B = cols_A
        cols_B = int(input("Enter the number of columns for Matrix B: "))
        if cols_B <= 0:
            print("Please enter a positive integer for columns of Matrix B.")
            continue
        break
    except ValueError:
        print("Input must be an integer. Please try again.")

A = input_matrix(rows_A, cols_A, "A")
B = input_matrix(rows_B, cols_B, "B")

print_matrix(A, "Matrix A")
print_matrix(B, "Matrix B")

try:
    C = multiply_matrices(A, B)
    print_matrix(C, "Result of Multiplication (A x B)")
except ValueError as e:
    print(f"Error: {e}")

print("\nThanks! Adios.")
