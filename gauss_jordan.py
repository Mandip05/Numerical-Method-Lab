def gauss_jordan(a, b):
    n = len(b)

    for i in range(n):
        # Partial pivoting: Swap rows if the diagonal element is zero
        if a[i][i] == 0:
            for k in range(i + 1, n):
                if a[k][i] != 0:
                    a[i], a[k] = a[k], a[i]
                    b[i], b[k] = b[k], b[i]
                    break
            else:
                raise ValueError("Singular matrix detected. No unique solution.")

        # Normalize the pivot row
        pivot = a[i][i]
        a[i] = [x / pivot for x in a[i]]
        b[i] /= pivot

        # Eliminate all other rows
        for j in range(n):
            if i != j:
                ratio = a[j][i]
                a[j] = [a[j][k] - ratio * a[i][k] for k in range(n)]
                b[j] -= ratio * b[i]

    return b


# Input handling
n = int(input("Enter the number of variables: "))

# Matrix coefficients
a = [list(map(float, input(f"Enter row {i + 1} coefficients (space-separated): ").split())) for i in range(n)]

# Constants
b = list(map(float, input("Enter the constants (space-separated): ").split()))

# Validate matrix dimensions
if len(b) != n or any(len(row) != n for row in a):
    print("Error: Invalid input dimensions.")
else:
    try:
        solution = gauss_jordan(a, b)
        print("\nSolution:")
        for i in range(n):
            print(f"x{i + 1} = {solution[i]:.6f}")
    except ValueError as e:
        print(f"Error: {e}")
