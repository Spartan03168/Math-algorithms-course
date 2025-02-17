import numpy as np
import sympy as sp
from Converters import numpy_conversion

def points_file_reader(file_name: str):
    assert(type(file_name) == str)

    point_detected = []
    with open(file_name, "r") as f:
        for line in f:
            x, y = map(float, line.strip().split(","))
            point_detected.append((x, y))
    # - Array conversion -
    return numpy_conversion(point_detected)

def legrange_interpolation(points, x_val):
    assert(isinstance(points, (list, np.ndarray)))

    points = numpy_conversion(points)
    x = sp.Symbol("x")
    n = len(points)
    polynomial = 0
    # -> For loop <-
    for elements in range(n):
        L = 1
        for internal_i in range(n):
            if elements != internal_i:
                L *= (x - points[internal_i, 0]) / (points[elements, 0] - points[int, 0])
        polynomial += points[elements, 1] * L
    # > Polynomial calculations complete <
    polynomial = sp.expand(polynomial)
    if x_val is not None:
        return polynomial, polynomial.evalf(subs={x: x_val})
    else:
        return polynomial, [-1]

def parametric_interpolation(points, x_val):
    assert(isinstance(points, (list, np.ndarray)))

    t = sp.Symbol('t')
    n = len(points)
    ts = np.linspace(0, 1, n)
    x_points, y_points = points[:, 0], points[:, 1]

    poly_x = legrange_interpolation(np.column_stack((ts, x_points)),x_val=None)
    poly_y = legrange_interpolation(np.column_stack((ts, y_points)), x_val=None)

    if x_val is not None:
        return (poly_x, poly_y), (poly_x.evalf(subs={t: x_val}), poly_y.evalf(subs={t: x_val}))
    else:
        return poly_x, poly_y, [-1]

def sle_interpolation(points, x_val):
    assert(isinstance(points, (list, np.ndarray)))

    n = len(points)
    a = np.vander(points[:, 0], N=n, increasing=True)
    coefficients = np.linalg.solve(a, points[:, 1])
    x = sp.Symbol("x")
    polynomial = sum(c * x**i for i, c in enumerate(coefficients))
    if x_val is not None:
        return polynomial, polynomial.evalf(subs={x: x_val})
    else:
        return polynomial, [-1]