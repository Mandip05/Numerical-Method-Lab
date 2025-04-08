def f(x):
    return 6*x*x-8*x+2
def fd(x):
    return 12*x-8
def newton_raphson(a,iteration,tol=0.001):
    for i in range(iteration):
        f_a=f(a)
        fd_a=fd(a) 
        x=a-(f(a)/fd(a))
        fx= f(x)
        print(f"Iteration(i+1):a={a}, x={x}, f{x}={fx}")
        if abs(fx)<tol:
            break
        a=x
        i+=1
        # print(f"\nThe root of the equation is approximately:")
        return x 


def main():
    n=float(input("Enter the value of a:"))
    iteration=int(input("Enter the number of iterations:"))
    root = newton_raphson(n,iteration)
    print(f"\nThe root of the equation is approximately:",{root})
if_name_ = "_main_"
main()