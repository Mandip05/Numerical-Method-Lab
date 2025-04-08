import math

# Define the function
def f(x):
    return math.cos(x)  # f(x) = sin(x)

def main():
    # Input lower and upper limits
    x0 = float(input("Enter Lower Limit (in radians): "))
    x1 = float(input("Enter Upper Limit (in radians): "))

    # Compute step size (h)
    h = (x1 - x0) / 2.0

    # Compute function values
    fx0 = f(x0)
    fx1 = f(x1)
    fx_mid = f(x0 + h)

    # Apply Simpson's 1/3 Rule formula
    v = (h / 3) * (fx0 + 4 * fx_mid + fx1)

    # Display result
    print(f"Value of Integration: {v:.6f}")

if __name__ == "__main__":
    main()
