import math

def f(x):
    return math.cos(x)  # Function definition

x0, x1 = map(float, input("Enter Lower and Upper Limit (in radians): ").split())
n = int(input("Enter number of intervals (multiple of 3): "))

h = (x1 - x0) / n

term = f(x0) + f(x1)

for i in range(1, n):
    x = x0 + i * h
    if i % 3 == 0:
        term += 2 * f(x)
    else:
        term += 3 * f(x)

v = (3 * h / 8) * term

print("Value of Integration:", v)
