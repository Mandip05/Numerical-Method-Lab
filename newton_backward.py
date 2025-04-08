n = int(input("Enter number of data points: "))
x = list(map(float, input("Enter x values: ").split()))
y = [list(map(float, input(f"Enter y value for x[{i}]: ").split())) for i in range(n)]

h = x[1] - x[0]
for j in range(1, n):
    for i in range(n - 1, j - 1, -1):
        y[i].append(y[i][j - 1] - y[i - 1][j - 1])

b1 = y[-1][1] / h
b2 = (y[-1][1] - (y[-1][2] / 2)) / h

print("First Derivative:", b1)
print("Second Derivative:", b2)
