def divided_difference(x, y):
    n = len(x)
    # Create a copy of y to store divided differences
    coeffs = y[:]  # Avoid modifying original y list
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            coeffs[j] = (coeffs[j] - coeffs[j - 1]) / (x[j] - x[j - i])
    return coeffs

# Taking input for x and y values
x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))
xp = float(input("Enter the point to interpolate: "))

# Compute the divided difference coefficients
coeffs = divided_difference(x, y)

# Compute the interpolated value using Newton's form
result = coeffs[0]
for i in range(1, len(x)):
    term = coeffs[i]
    for j in range(i):
        term *= (xp - x[j])
    result += term

# Display the interpolated result
print("Interpolated value:", result)
