import math

# Function definitions (Picard's approximations)
def y1(x):
    return math.sin(x) + x**3 - 2*x

def y2(x):
    return 1 + x - (x**2)/2 + (x**3)/6 + x**3 - 2*x

def y3(x):
    return 1 + x - (x**2)/2 + (x**3)/6 - (x**4)/24 + x**3 - 2*x

def main():
    # User input
    x0 = float(input("Enter initial value of x: "))
    y0 = float(input("Enter initial value of y: "))
    x = float(input("Enter x at which function is to be evaluated: "))

    # Compute function values iteratively (Picard's method)
    y = y0  # Start with initial value
    y += y1(x)  # First approximation
    y += y2(x)  # Second approximation
    y += y3(x)  # Third approximation

    print(f"\nFunction Value at x = {x:.6f} is {y:.6f}")

if __name__ == "__main__":
    main()
