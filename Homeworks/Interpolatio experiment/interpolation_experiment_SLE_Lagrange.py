import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.linalg import solve

# ----> Functions <----
def interpolate_sle(x_points, y_points):
    n = len(x_points)
    A = np.vander(x_points, increasing=True)
    coefficients = solve(A, y_points)
    return lambda x: sum(coefficients[i] * x ** i for i in range(n))

def interpolation_process(f, x_points: [list, np.ndarray], title: str, chart_fabrication: int, developer_mode: int):
    y_points = f(x_points)
    # ---> Calculations <---
    if developer_mode == 1:
        print(f"Title: {title}")
        print("Calculations in progress...")
    sle_poly = interpolate_sle(x_points,y_points)
    lagrange_poly = lagrange(x_points, y_points)

    x_fine = np.linspace(min(x_points), max(x_points), 300)
    y_fine = f(x_fine)
    y_sle = [sle_poly(x) for x in x_fine]
    y_lagrange = lagrange_poly(x_fine)

    # ---> Chart fabrication <---
    if developer_mode == 1:
        if chart_fabrication == 1:
            print("Charting in progress...")
        elif chart_fabrication != 1:
            print("Charting disabled...")
    if chart_fabrication == 1:
        plt.figure(figsize=(8, 6))
        plt.plot(x_fine, y_fine, 'k-', label='Original Function')
        plt.plot(x_fine, y_sle, 'r--', label='SLE Interpolation')
        plt.plot(x_fine, y_lagrange, 'b-.', label='Lagrange Interpolation')
        plt.scatter(x_points, y_points, color='black', zorder=3, label='Interpolation Points')

        plt.legend()
        plt.title(title)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid()
        plt.show()
        plt.close()
        if developer_mode == 1:
            print("Charting process complete")

    if developer_mode == 1:
        print(f"Current title processing completion\n")
    return sle_poly, lagrange_poly, y_lagrange

# Deployment
dev_mode = 1
chart_fab_key = 1

x_points = np.linspace(0, 4, 6)
sin_func_1_sle_poly, sin_func_1_lagrange_poly, sin_func_1_y_lagrange = interpolation_process(np.sin, x_points, "Interpolation of sin(x) on [0,4]", chart_fabrication=chart_fab_key, developer_mode=dev_mode)
sin_func_2_sle_poly, sin_func_2_lagrange_poly, sin_func_2_y_lagrange = interpolation_process(lambda x: np.sin(3 * x), x_points, "Interpolation of sin(3x) on [0,4]", chart_fabrication=chart_fab_key, developer_mode=dev_mode)
sin_func_3_sle_poly, sin_func_3_lagrange_poly, sin_func_3_y_lagrange = interpolation_process(lambda x: np.sin(5 * x), x_points, "Interpolation of sin(5x) on [0,4]", chart_fabrication=chart_fab_key, developer_mode=dev_mode)