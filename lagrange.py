def lagrange(x, y, xp):
    result = 0
    for i in range(len(x)):
        term = y[i]
        for j in range(len(x)):
            if j != i:
                term *= (xp - x[j]) / (x[i] - x[j])
        result += term
    return result

# Taking input for x and y values
x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))
xp = float(input("Enter the point to interpolate: "))

# Calculating the interpolated value
print("Interpolated value:", lagrange(x, y, xp))
