def forward_difference(x, y, xp):
    n = len(x)
    # Create a difference table
    diff_table = [y[:] ]  # Copy the original y values as the first row

    for i in range(1, n):
        diff_table.append([0] * (n - i))  # Create space for new differences
        for j in range(n - i):
            diff_table[i][j] = diff_table[i-1][j+1] - diff_table[i-1][j]

    # Compute the interpolated value using Newton's Forward Difference Formula
    result = y[0]
    h = x[1] - x[0]  # Step size
    p = (xp - x[0]) / h  # Calculate p
    fact = 1

    for i in range(1, n):
        fact *= (p - i + 1) / i
        result += fact * diff_table[i][0]  # Use first element from each row

    return result

# Taking input for x and y values
x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))
xp = float(input("Enter the point to interpolate: "))

# Compute and display the interpolated value
print("Interpolated value:", forward_difference(x, y, xp))
