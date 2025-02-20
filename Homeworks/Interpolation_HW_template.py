import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def read_points_from_file(filename):
    points = []
    with open(filename, 'r') as f:
        for line in f:
            x, y = map(float, line.strip().split(','))
            points.append((x, y))
    return np.array(points)

def lagrange_interpolation(points, x_val=None):
    x = sp.Symbol('x')
    n = len(points)
    polynomial = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (x - points[j, 0]) / (points[i, 0] - points[j, 0])
        polynomial += points[i, 1] * L
    polynomial = sp.expand(polynomial)
    if x_val is not None:
        return polynomial, polynomial.evalf(subs={x: x_val})
    return polynomial

def sle_interpolation(points, x_val=None):
    n = len(points)
    A = np.vander(points[:, 0], N=n, increasing=True)
    coeffs = np.linalg.solve(A, points[:, 1])
    x = sp.Symbol('x')
    polynomial = sum(c * x**i for i, c in enumerate(coeffs))
    if x_val is not None:
        return polynomial, polynomial.evalf(subs={x: x_val})
    return polynomial

def parametric_interpolation(points, x_val=None):
    t = sp.Symbol('t')
    n = len(points)
    ts = np.linspace(0, 1, n)
    x_points, y_points = points[:, 0], points[:, 1]

    poly_x = lagrange_interpolation(np.column_stack((ts, x_points)))
    poly_y = lagrange_interpolation(np.column_stack((ts, y_points)))

    if x_val is not None:
        return (poly_x, poly_y), (poly_x.evalf(subs={t: x_val}), poly_y.evalf(subs={t: x_val}))
    return poly_x, poly_y

def plot_interpolations(points, polys):
    x_vals = np.linspace(min(points[:,0]), max(points[:,0]), 1000)
    plt.scatter(points[:,0], points[:,1], color='red', label='Data points')
    for name, poly in polys.items():
        y_vals = [poly.evalf(subs={sp.Symbol('x'): x}) for x in x_vals]
        plt.plot(x_vals, y_vals, label=name)
    plt.legend()
    plt.show()

def main():
    print("Interpolation Tool")
    choice = input("Choose input method (1: Function, 2: File): ")

    if choice == '1':
        func_expr = input("Enter function of x: ")
        a, b = map(float, input("Enter interval [a, b]: ").split())
        deg = int(input("Enter polynomial degree: "))
        func = sp.sympify(func_expr)
        x_vals = np.linspace(a, b, deg+1)
        points = np.array([[x, func.evalf(subs={sp.Symbol('x'): x})] for x in x_vals])
    else:
        filename = input("Enter filename: ")
        points = read_points_from_file(filename)

    print("Select methods:")
    methods = []
    if input("SLE? (y/n): ") == 'y':
        methods.append(('SLE', sle_interpolation(points)))
    if input("Lagrange? (y/n): ") == 'y':
        methods.append(('Lagrange', lagrange_interpolation(points)))
    if input("Parametric? (y/n): ") == 'y':
        methods.append(('Parametric', parametric_interpolation(points)))

    plot_interpolations(points, dict(methods))

    while True:
        calc = input("Calculate value at x (enter to quit): ")
        if not calc:
            break
        x_val = float(calc)
        for name, poly in methods:
            if isinstance(poly, tuple):
                val = (poly[0].evalf(subs={sp.Symbol('t'): x_val}), poly[1].evalf(subs={sp.Symbol('t'): x_val}))
            else:
                val = poly.evalf(subs={sp.Symbol('x'): x_val})
            print(f"{name} interpolation at x={x_val}: {val}")

if __name__ == "__main__":
    main()