# Function to calculate factorial
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

def main():
    # User input for number of points
    n = int(input("Enter the number of points: "))

    # Arrays for x, f(x), and forward differences
    x = [0] * n
    fx = [0] * n
    fd = [0] * n

    # Input values for x and f(x)
    print("Enter values of x and f(x): ")
    for i in range(n):
        x[i], fx[i] = map(float, input().split())

    # Input the value at which derivative is needed
    xp = float(input("Enter the value at which derivative is needed: "))

    # Compute step size (h) and parameter (s)
    h = x[1] - x[0]
    s = (xp - x[0]) / h

    # Initialize forward difference array
    fd[:] = fx[:]

    # Compute forward differences
    for i in range(n):
        for j in range(n - 1, i, -1):
            fd[j] = fd[j] - fd[j - 1]

    # Compute first derivative
    val = fd[1]
    prev = 0
    for i in range(2, n):
        term1 = 1
        for k in range(2, i + 1):
            term1 *= (s - k + 2)
        term2 = (s - i + 1) * prev
        prev = term1 + term2
        val += (fd[i] * (term1 + term2)) / fact(i)

    val = val / h

    # Display result
    print(f"Value of First Derivative = {val:.6f}")

if __name__ == "__main__":
    main()
