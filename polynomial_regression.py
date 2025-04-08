def gaussian_elimination(a, b):
    """Solve a system of linear equations using Gaussian elimination."""
    n = len(b)
    # Augment matrix a with vector b
    for i in range(n):
        a[i].append(b[i])

    # Perform Gaussian elimination
    for i in range(n):
        # Pivot: Find the row with the largest element in column i
        max_row = max(range(i, n), key=lambda r: abs(a[r][i]))
        a[i], a[max_row] = a[max_row], a[i]
        
        # Eliminate column i
        for j in range(i + 1, n):
            factor = a[j][i] / a[i][i]
            for k in range(i, n + 1):
                a[j][k] -= a[i][k] * factor

    # Back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = a[i][n] / a[i][i]
        for j in range(i - 1, -1, -1):
            a[j][n] -= a[j][i] * x[i]

    return x

def polynomial_regression():
    n = int(input("Enter the number of points: "))  
    m = int(input("Enter degree of polynomial to be fitted: "))  

    if m >= n:  
        print("Error: Degree of polynomial must be less than the number of points!")  
        return  

    x = []  
    y = []  

    print("Enter the values of x and y:")  
    for i in range(n):  
        xi, yi = map(float, input(f"Point {i+1} (x and y): ").split())  
        x.append(xi)  
        y.append(yi)  

    # Create Vandermonde matrix
    X = [[xi**j for j in range(m+1)] for xi in x]
    
    # Solve the normal equation: (X^T * X) * a = X^T * y
    Xt = [[X[j][i] for j in range(n)] for i in range(m+1)]  # Transpose of X
    XtX = [[sum(Xt[i][k] * X[k][j] for k in range(n)) for j in range(m+1)] for i in range(m+1)]
    XtY = [sum(Xt[i][j] * y[j] for j in range(n)) for i in range(m+1)]
    
    # Use Gaussian elimination to solve XtX * a = XtY
    coefficients = gaussian_elimination(XtX, XtY)

    # Output the polynomial equation
    print("\nThe polynomial equation is:")
    terms = [f"{coefficients[i]:.3f} x^{i}" if i > 0 else f"{coefficients[i]:.3f}"  
             for i in range(len(coefficients)) if abs(coefficients[i]) > 1e-6]  
    equation = "y = " + " + ".join(terms)  

    print(equation)

polynomial_regression()
