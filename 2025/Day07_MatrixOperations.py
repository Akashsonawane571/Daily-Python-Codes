# Day07_MatrixOperations.py
# Perform Matrix Transpose and Multiplication

def transpose(matrix):
    """Return the transpose of a matrix"""
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def multiply_matrix(A, B):
    """Multiply two matrices"""
    if len(A[0]) != len(B):
        raise ValueError("Matrix A's column count must equal Matrix B's row count")
    
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


if __name__ == "__main__":
    # Example matrices
    A = [[1, 2, 3],
         [4, 5, 6]]

    B = [[7, 8],
         [9, 10],
         [11, 12]]

    print("Matrix A:", A)
    print("Matrix B:", B)

    print("\nTranspose of A:", transpose(A))
    print("Transpose of B:", transpose(B))

    print("\nMultiplication of A and B:", multiply_matrix(A, B))
