def linear_regression(x, y):
    n = len(x)
    
    # Compute means of x and y
    x_mean = sum(x) / n
    y_mean = sum(y) / n
    
    # Compute required summations
    xy_sum = sum(x[i] * y[i] for i in range(n))
    xx_sum = sum(x[i] ** 2 for i in range(n))
    
    # Compute slope (b1) and intercept (b0)
    b1 = (xy_sum - n * x_mean * y_mean) / (xx_sum - n * x_mean ** 2)
    b0 = y_mean - b1 * x_mean
    
    return b0, b1

# Taking input for x and y values
x = list(map(float, input("Enter x values (space-separated): ").split()))
y = list(map(float, input("Enter y values (space-separated): ").split()))

# Ensure x and y have the same number of elements
if len(x) != len(y):
    print("Error: x and y must have the same number of values.")
else:
    b0, b1 = linear_regression(x, y)
    print(f"Linear Regression Equation: y = {b0:.4f} + {b1:.4f}x")
