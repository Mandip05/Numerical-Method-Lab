import math

MAX = 10  # Maximum grid size

def solve_heat_equation():
    # Input grid size
    n = int(input("Enter the dimension of plate (n,n): "))
    if n > MAX or n < 2:
        print(f"Grid size must be between 2 and {MAX}")
        return
    
    # Input boundary conditions
    tL, tR, tT, tB = map(float, input("Enter temperatures at left, right, top, and bottom: ").split())
    
    size = n * n  # Total number of points
    
    # Initialize coefficient matrix (as a list of lists)
    a = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        a[i][i] = -4  # Center point
        row = i // n
        col = i % n
        if row > 0:
            a[i][i - n] = 1  # Top neighbor
        if row < n - 1:
            a[i][i + n] = 1  # Bottom neighbor
        if col > 0:
            a[i][i - 1] = 1  # Left neighbor
        if col < n - 1:
            a[i][i + 1] = 1  # Right neighbor
    
    # Initialize right-hand side vector with boundary conditions
    b = [0] * size
    for i in range(size):
        row = i // n
        col = i % n
        if row == 0:
            b[i] -= tT  # Top boundary
        if row == n - 1:
            b[i] -= tB  # Bottom boundary
        if col == 0:
            b[i] -= tL  # Left boundary
        if col == n - 1:
            b[i] -= tR  # Right boundary
    
    # Input accuracy limit
    error = float(input("Enter accuracy limit: "))
    
    # Initialize guess
    old_x = [0.0] * size
    new_x = [0.0] * size
    E = [0.0] * size
    
    # Gauss-Seidel iteration
    max_iter = 1000
    for k in range(max_iter):
        for i in range(size):
            sum_val = b[i]
            for j in range(size):
                if i != j:
                    sum_val -= a[i][j] * old_x[j]
            new_x[i] = sum_val / a[i][i]
            E[i] = abs(new_x[i] - old_x[i]) / (abs(new_x[i]) + 1e-10)  # Avoid division by zero
        
        # Check convergence
        converged = all(e <= error for e in E)
        if converged:
            print(f"Converged after {k + 1} iterations")
            break
        
        if k == max_iter - 1:
            print("Warning: Maximum iterations reached")
        
        old_x = new_x[:]
    
    # Output solution as 2D grid
    print("\nTemperature Distribution:")
    for i in range(n):
        row = [new_x[i * n + j] for j in range(n)]
        print(" ".join(f"{val:8.4f}" for val in row))

# Run the solver
if __name__ == "__main__":
    solve_heat_equation()