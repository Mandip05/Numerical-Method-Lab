def jacobi_iteration(a, b, tol=1e-6, max_iter=1000):
    n = len(b)
    x = [0] * n  # Initial guess
    x_new = x[:]

    for iteration in range(max_iter):
        for i in range(n):
            if a[i][i] == 0:
                raise ValueError("Zero diagonal element detected. Jacobi method cannot proceed.")
            
            s = sum(a[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / a[i][i]

        # Convergence check
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new, iteration + 1  # Return solution and iteration count
        
        x = x_new[:]  # Update x values
    
    raise ValueError("Jacobi method did not converge within the maximum iterations.")


# Input Handling
n = int(input("Enter matrix size: "))
a = [list(map(float, input(f"Enter row {i+1}: ").split())) for i in range(n)]
b = list(map(float, input("Enter RHS values: ").split()))


# Ensure the matrix is square
if any(len(row) != n for row in a):
    print("Error: The matrix must be square.")
else:
    try:
        solution, iterations = jacobi_iteration(a, b)
        print("\nSolution:")
        for i, val in enumerate(solution):
            print(f"x{i+1} = {val:.6f}")
        print(f"Converged in {iterations} iterations.")

    except ValueError as e:
        print(f"Error: {e}")
