def f(x):
    return x * x + 4 * x + 2  # Function definition

x0, x1 = map(float, input("Enter Lower and Upper Limit: ").split())

h = x1 - x0
fx0 = f(x0)
fx1 = f(x1)
v = h / 2 * (fx0 + fx1)

print("Value of Integration:", v)
