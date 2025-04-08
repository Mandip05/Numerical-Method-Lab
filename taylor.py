import math

# Factorial function (recursive)
def fact(n):
    return 1 if n == 1 else n * fact(n - 1)

# Function to evaluate the Taylor series
def taylor_series(x0, yx0, x):
    fdy = (x0)**2 + (yx0)**2  # First derivative
    sdy = 2*x0 + 2*yx0*fdy    # Second derivative
    tdy = 2 + 2*yx0*sdy + 2*fdy**2  # Third derivative

    # Taylor series expansion up to third-order term
    yx = (yx0 
          + (x - x0) * fdy 
          + ((x - x0) * sdy) / fact(2) 
          + ((x - x0)**3 * tdy) / fact(3))

    return yx

def main():
    # User input
    x0 = float(input("Enter initial value of x: "))
    yx0 = float(input("Enter initial value of y: "))
    x = float(input("Enter x at which function is to be evaluated: "))

    result = taylor_series(x0, yx0, x)
    
    print(f"\nFunction Value at x = {x:.6f} is {result:.6f}")

if __name__ == "__main__":
    main()
