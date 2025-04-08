import math

def f(x):
    return x * x * x + 4  # Function definition

a, b = map(float, input("Enter Lower and Upper Limit: ").split())

# Gaussian points
z1, z2 = -0.57735, 0.57735

# Transform integration limits
x1 = ((b - a) / 2) * z1 + (b + a) / 2
x2 = ((b - a) / 2) * z2 + (b + a) / 2

# Gaussian Quadrature Formula
v = ((b - a) / 2) * (f(x1) + f(x2))

# Display result
print("Value of Integration = {:.6f}".format(v))
