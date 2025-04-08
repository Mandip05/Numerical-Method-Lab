def f(x):
    return 5 * (x) * (x) + 3 * (x) - 2  # Function definition

x0, xn = map(float, input("Enter Lower and Upper Limit: ").split())
k = int(input("Enter Number of Segments: "))

h = (xn - x0) / k
fx0 = f(x0)
fxn = f(xn)
term = fx0 + fxn

for i in range(1, k):
    a = x0 + i * h
    term += 2 * f(a)

v = (h / 2) * term

print("Value of Integration:", v)
