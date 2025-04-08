def lu_decomposition(a, n):
    # Initialize L and U matrices
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]

    for i in range(n):
        L[i][i] = 1  # Set diagonal of L to 1

        # Compute U (Upper Triangular)
        for j in range(i, n):
            U[i][j] = a[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

        # Compute L (Lower Triangular)
        for j in range(i + 1, n):
            if U[i][i] == 0:
                raise ValueError("Zero pivot encountered! LU decomposition fails.")
            L[j][i] = (a[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U


# Input Handling
n = int(input("Enter matrix size: "))
a = [list(map(float, input(f"Enter row {i+1}: ").split())) for i in range(n)]

# Ensure the matrix is square
if any(len(row) != n for row in a):
    print("Error: The matrix must be square.")
else:
    try:
        L, U = lu_decomposition(a, n)

        print("\nL Matrix:")
        for row in L:
            print(" ".join(f"{val:.6f}" for val in row))

        print("\nU Matrix:")
        for row in U:
            print(" ".join(f"{val:.6f}" for val in row))

    except ValueError as e:
        print(f"Error: {e}")
