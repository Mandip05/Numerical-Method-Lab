def f(x):
    return x * x - 6 * x - 4


def bisection_method(a, b, iteration, error=0.001):
    if f(a) * f(b) >= 0:
        print("The chosen interval does not satisfy the bisection method requirements.")
        return None

    print(f"{'Iteration':>10} {'a':>10} {'b':>10} {'c':>15} {'f(c)':>15}")
    for i in range(iteration):
        c = (a + b) / 2
        fc = f(c)
        print(f"{i + 1:>10} {a:>10.6f} {b:>10.6f} {c:>15.6f} {fc:>15.6f}")

        if abs(fc) < error or abs(b - a) < error:
            print("\nConvergence achieved!")
            return c

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return c


def main():
    a = float(input("Enter the lower bound (a): "))
    b = float(input("Enter the upper bound (b): "))
    iteration = int(input("Enter the number of iterations: "))
    root = bisection_method(a, b, iteration)
    if root is not None:
        print(f"\nThe root of the equation is approximately: {root:.6f}")


if __name__ == "__main__":
    main()
