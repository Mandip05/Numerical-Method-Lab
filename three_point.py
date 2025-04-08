def f(x):
    return 4 * (x) * (x) + 2  # Function definition

x = float(input("Enter the value at which derivative is required: "))
h = float(input("Enter increment h: "))

# Central Difference Formula
d = (f(x + h) - f(x - h)) / (2 * h)

print("Value of Derivative =", d)
