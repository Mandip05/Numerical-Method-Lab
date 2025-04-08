def honer(coefficients, x):
    result = coefficients[0]
    for i in range(1, len(coefficients)):
        result = result * x + coefficients[i]
    return result

coefficients = [4, 2, -1, 25] # Example coefficients for the polynomial 4x^3 + 2x^2 - 1x + 25
x = float(input("Enter the value of x: "))
result = honer(coefficients, x)
print(f"Result of polynomial evaluation: {result}")
