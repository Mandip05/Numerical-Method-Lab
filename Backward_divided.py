def u_cal(u, n):
    """Calculate u(u+1)(u+2)...(u+n-1)"""
    temp = u
    for i in range(1, n):
        temp *= (u + i)
    return temp

def fact(n):
    """Calculate factorial of n"""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

# Number of data points
n = 4

# Given data points
x = [45, 50, 55, 60]
y = [[0 for i in range(n)] for j in range(n)]

# Initial values (function values)
y[0][0] = 0.7071
y[1][0] = 0.7660
y[2][0] = 0.8192
y[3][0] = 0.8660

# Creating the backward difference table
for i in range(1, n):
    for j in range(n - 1, i - 1, -1):
        y[j][i] = y[j][i - 1] - y[j - 1][i - 1]

# Displaying the backward difference table
print("Backward Difference Table:")
for i in range(n):
    print(x[i], end="\t")
    for j in range(i + 1):
        print(round(y[i][j], 6), end="\t")
    print("")

# Value to interpolate
value = 52

# Calculating the interpolated value using Newton's Backward Interpolation formula
sum = y[n - 1][0]  # Start with last y-value
h = x[1] - x[0]  # Step size
u = (value - x[n - 1]) / h  # Compute u

for i in range(1, n):
    sum += (u_cal(u, i) * y[n - 1][i]) / fact(i)

print(f"\nValue at {value} is {round(sum, 6)}")
