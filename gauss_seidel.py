def gauss_seidel(a, b, tol=1e-6, max_iter=1000):
    n = len(b)
    x = [0] * n  # Initial guess

    for iteration in range(max_iter):
        x_old = x[:]  # Store previous iteration values

        for i in range(n):
            if a[i][i] == 0:
                raise ValueError("Zero diagonal element detected. Gauss-Seidel method cannot proceed.")

            s = sum(a[i][j] * x[j] for j in range(n) if j != i)  # Use updated values immediately
            x[i] = (b[i] - s) / a[i][i]

        # Convergence check
        if all(abs(x[i] - x_old[i]) < tol for i in range(n)):
            return x, iteration + 1  # Return solution and iteration count

    raise ValueError("Gauss-Seidel method did not converge within the maximum iterations.")


# Input Handling
n = int(input("Enter matrix size: "))
a = [list(map(float, input(f"Enter row {i+1}: ").split())) for i in range(n)]
b = list(map(float, input("Enter RHS values: ").split()))


# Ensure the matrix is square
if any(len(row) != n for row in a):
    print("Error: The matrix must be square.")
else:
    try:
        solution, iterations = gauss_seidel(a, b)
        print("\nSolution:")
        for i, val in enumerate(solution):
            print(f"x{i+1} = {val:.6f}")
        print(f"Converged in {iterations} iterations.")

    except ValueError as e:
        print(f"Error: {e}")
