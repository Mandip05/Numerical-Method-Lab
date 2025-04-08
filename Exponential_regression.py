# Write a python program for Exponential Regression.

import math  
def exponential_regression():  
    n = int(input("Enter the number of points: "))  
    x = []  
    y = []  
    Y = []  

    print("Enter the values of x and y:")  
    for i in range(n):  
        xi, yi = map(float, input(f"Point {i+1} (x and y): ").split())  

        x.append(xi)  
        y.append(yi)  
        Y.append(math.log(yi))  

    sumX = sum(x)  
    sumY = sum(Y)  
    sumX2 = sum(xi ** 2 for xi in x)  
    sumXY = sum(x[i] * Y[i] for i in range(n))  

    A = ((sumX2 * sumY - sumX * sumXY) / (n * sumX2 - sumX ** 2))  
    b = ((n * sumXY - sumX * sumY) / (n * sumX2 - sumX ** 2))  
    a = math.exp(A)  

    print(f"\nThe curve is: y = {a:.3f} e^({b:.3f} x)")  

exponential_regression()
