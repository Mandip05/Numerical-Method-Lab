def f(x):
    return x * x + 4 * x + 8

def secant_method(a, b, max_iteration, error=0.001):
    for i in range(max_iteration):
        f_a = f(a)
        f_b = f(b)
        #for the secant method
        x = a - (f_a * (a - b) / (f_a - f_b))
        fx = f(x)
        print(f"Iteration {i+1}: a={a}, b={b}, x={x}, f(x)={fx}")
        
        if abs(fx) < error:
            break
        
        
        a, b = b, x
    
    return x

def main():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    max_iteration = int(input("Enter the number of iterations: "))
    root = secant_method(a, b, max_iteration)
    print(f"\nThe root of the equation is approximately: {root}")

if __name__ == "__main__":
    main()
