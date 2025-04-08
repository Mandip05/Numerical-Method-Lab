def f(x):
    return x * x - 6 * x - 4


def g(x):
    return (x * x - 4) / 6


def fixed_point_method(x0, iteration, error=0.001):
    print(f"{'Iteration':>10} {'x':>15} {'f(x)':>15}")
    for i in range(iteration):
        x1 = g(x0)
        fx = f(x1)
        print(f"{i + 1:>10} {x1:>15.6f} {fx:>15.6f}")
        if abs(x1 - x0) < error:
            print("\nConvergence achieved!")
            return x1
        x0 = x1
    return x1


def main():
    x0 = float(input("Enter the initial guess: "))
    iteration = int(input("Enter the number of iterations: "))
    root = fixed_point_method(x0, iteration)
    print(f"\nThe root of the equation is approximately: {root:.6f}")


if __name__ == "__main__":
    main()
