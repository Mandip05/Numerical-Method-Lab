def f(x, y):
    return 2 * x + y  # Define the function f(x, y)

# Input values
x0 = float(input("Enter initial value of x (x0): "))
y0 = float(input("Enter initial value of y (y0): "))
xp = float(input("Enter x at which function is to be evaluated (xp): "))
h = float(input("Enter step size (h): "))

x = x0
y = y0

while x < xp:
    m1 = f(x, y)
    m2 = f(x + h / 2, y + (h / 2) * m1)
    m3 = f(x + h / 2, y + (h / 2) * m2)
    m4 = f(x + h, y + h * m3)

    y = y + (h / 6) * (m1 + 2 * m2 + 2 * m3 + m4)
    x += h

print(f"Function value at x = {xp:.2f} is y = {y:.4f}")
