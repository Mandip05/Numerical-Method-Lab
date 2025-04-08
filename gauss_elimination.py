def gauss_elimination(a, b):
    n = len(b)

    # Forward elimination
    for i in range(n):
        if a[i][i] == 0:
            raise ValueError("Mathematical error: Division by zero detected!")

        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]
            for k in range(n):
                a[j][k] -= ratio * a[i][k]
            b[j] -= ratio * b[i]

    # Back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= a[i][j] * x[j]
        x[i] /= a[i][i]

    return x

# Taking input for augmented matrix
n = int(input("Enter the number of variables: "))

# Matrix coefficients
a = [list(map(float, input(f"Enter row {i + 1} coefficients (space-separated): ").split())) for i in range(n)]

# Constants
b = list(map(float, input("Enter the constants (space-separated): ").split()))

# Ensure matrix is valid
if len(b) != n or any(len(row) != n for row in a):
    print("Error: Invalid input dimensions.")
else:
    try:
        solution = gauss_elimination(a, b)
        print("\nSolution:")
        for i in range(n):
            print(f"x{i + 1} = {solution[i]:.4f}")
    except ValueError as e:
        print(f"Error: {e}")
