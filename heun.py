# Function definition
def f(x, y):
    return 2 * y / x

def modified_euler():
    # User input
    x0 = float(input("Enter initial value of x: "))
    y0 = float(input("Enter initial value of y: "))
    xp = float(input("Enter x at which function is to be evaluated: "))
    h = float(input("Enter the step size: "))

    # Initialization
    y = y0
    x = x0

    # Modified Euler's Method
    while x < xp:
        m1 = f(x, y)
        m2 = f(x + h, y + h * m1)
        y = y + (h / 2) * (m1 + m2)
        x += h  # Increment x

    # Output the result
    print(f"Function Value at x = {xp:.6f} is {y:.6f}")

# Run the function
if __name__ == "__main__":
    modified_euler()
