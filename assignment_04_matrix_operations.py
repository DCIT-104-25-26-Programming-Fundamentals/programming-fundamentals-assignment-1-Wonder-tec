# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#



def read_matrix(name="matrix"):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    matrix = []
    for i in range(rows):
        row_input = input(f"Enter row {i + 1}: ")
        row = [int(x) for x in row_input.split()]
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:4}" for val in row))
    print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


def main():
    print("=== PART A: Transpose a Matrix ===")
    matrix = read_matrix("the matrix")
    print("\nOriginal Matrix:")
    display_matrix(matrix)
    print("Transposed Matrix:")
    display_matrix(transpose_matrix(matrix))

    print("=== PART B: Add Two Matrices ===")
    print("Matrix A:")
    matrix_a = read_matrix("Matrix A")
    print("Matrix B (must be same size as Matrix A):")
    matrix_b = read_matrix("Matrix B")

    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])

    if rows_a != rows_b or cols_a != cols_b:
        print("Error: Matrices must be the same size to add.")
    else:
        print("\nSum of Matrices:")
        display_matrix(add_matrices(matrix_a, matrix_b))

    print("=== PART C: Multiply Two Matrices ===")
    print("Matrix A (M x N):")
    matrix_a2 = read_matrix("Matrix A")
    print("Matrix B (N x P):")
    matrix_b2 = read_matrix("Matrix B")

    cols_a2 = len(matrix_a2[0])
    rows_b2 = len(matrix_b2)

    if cols_a2 != rows_b2:
        print("Error: Number of columns in A must equal number of rows in B.")
    else:
        print("\nProduct of Matrices:")
        display_matrix(multiply_matrices(matrix_a2, matrix_b2))


if __name__ == "__main__":
    main()

