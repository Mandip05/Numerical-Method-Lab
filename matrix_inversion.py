def gauss_jordan_inverse(a):
    n = len(a)
    
    # Create an identity matrix of the same size as A
    I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    
    for i in range(n):
        # Pivoting: Swap rows if the pivot element is zero
        if a[i][i] == 0:
            for k in range(i + 1, n):
                if a[k][i] != 0:
                    a[i], a[k] = a[k], a[i]  # Swap rows in matrix
                    I[i], I[k] = I[k], I[i]  # Swap rows in identity matrix
                    break
            else:
                raise ValueError("Singular matrix detected. Inverse does not exist.")

        # Normalize pivot row
        pivot = a[i][i]
        a[i] = [x / pivot for x in a[i]]
        I[i] = [x / pivot for x in I[i]]

        # Eliminate other rows
        for j in range(n):
            if i != j:
                ratio = a[j][i]
                a[j] = [a[j][k] - ratio * a[i][k] for k in range(n)]
                I[j] = [I[j][k] - ratio * I[i][k] for k in range(n)]

    return I


# Input Handling
n = int(input("Enter the number of rows/columns of the matrix: "))

# Read the matrix
a = [list(map(float, input(f"Enter row {i + 1} (space-separated values): ").split())) for i in range(n)]

# Ensure the matrix is square
if any(len(row) != n for row in a):
    print("Error: The matrix must be square.")
else:
    try:
        inverse = gauss_jordan_inverse(a)
        print("\nInverse Matrix:")
        for row in inverse:
            print(" ".join(f"{val:.6f}" for val in row))  # Format for better readability
    except ValueError as e:
        print(f"Error: {e}")
