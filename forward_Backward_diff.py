def forward_backward_difference(x, y):
    n = len(x)

    # Check if spacing is uniform
    h = [x[i + 1] - x[i] for i in range(n - 1)]
    if any(abs(h[i] - h[0]) > 1e-6 for i in range(1, len(h))):
        raise ValueError("x-values are not equally spaced!")

    # Forward Differences (for first n-1 points)
    fwd_diff = [(y[i + 1] - y[i]) / h[i] for i in range(n - 1)]

    # Backward Differences (for last n-1 points)
    bwd_diff = [(y[i] - y[i - 1]) / h[i - 1] for i in range(1, n)]

    return fwd_diff, bwd_diff

# Input Handling
x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))

if len(x) != len(y):
    print("Error: x and y values must have the same length.")
else:
    try:
        fwd_diff, bwd_diff = forward_backward_difference(x, y)
        print("\nForward Differences:")
        for i, val in enumerate(fwd_diff):
            print(f"f'({x[i]}) ≈ {val:.6f}")

        print("\nBackward Differences:")
        for i, val in enumerate(bwd_diff):
            print(f"f'({x[i+1]}) ≈ {val:.6f}")

    except ValueError as e:
        print(f"Error: {e}")
