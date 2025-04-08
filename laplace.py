def solve_heat_equation(n, tL, tR, tT, tB, error_limit):
    # Coefficient matrix and solution vectors
    a = [[0] * (n * n) for _ in range(n * n)]
    b = [0] * (n * n)
    new_x = [0] * (n * n)
    old_x = [0] * (n * n)

    # Initialize coefficient matrix
    for i in range(n):
        for j in range(n):
            row_index = i * n + j
            a[row_index][row_index] = -4  # Main diagonal
            if i > 0:
                a[row_index][(i - 1) * n + j] = 1  # Top neighbor
            if i < n - 1:
                a[row_index][(i + 1) * n + j] = 1  # Bottom neighbor
            if j > 0:
                a[row_index][i * n + (j - 1)] = 1  # Left neighbor
            if j < n - 1:
                a[row_index][i * n + (j + 1)] = 1  # Right neighbor

    # Apply boundary conditions to vector b
    for i in range(n):
        for j in range(n):
            row_index = i * n + j
            if i == 0:
                b[row_index] -= tT  # Top boundary
            if i == n - 1:
                b[row_index] -= tB  # Bottom boundary
            if j == 0:
                b[row_index] -= tL  # Left boundary
            if j == n - 1:
                b[row_index] -= tR  # Right boundary

    # Iterative solution using Gauss-Seidel method
    while True:
        E = [0] * (n * n)
        for i in range(n * n):
            if a[i][i] == 0:
                continue  # Avoid division by zero
            sum_value = b[i] - sum(a[i][j] * old_x[j] for j in range(n * n)) + (a[i][i] * old_x[i])
            new_x[i] = sum_value / a[i][i]
            E[i] = abs(new_x[i] - old_x[i]) / (abs(new_x[i]) + 1e-10)  # Avoid division by zero
        
        if all(e < error_limit for e in E):
            break
        
        old_x = new_x[:]  # Update old_x with new values

    # Reshape solution into 2D format
    solution = [[new_x[i * n + j] for j in range(n)] for i in range(n)]
    return solution

# User input
n = int(input("Enter the dimension of plate (n,n): "))
tL, tR, tT, tB = map(float, input("Enter temperatures at left, right, top, and bottom: ").split())
error_limit = float(input("Enter accuracy limit: "))

solution = solve_heat_equation(n, tL, tR, tT, tB, error_limit)

print("Solution:")
for row in solution:
    print(row)
