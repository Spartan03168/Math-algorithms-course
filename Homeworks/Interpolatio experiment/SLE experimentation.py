import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.linalg import solve

# ------------------> Functions <------------------
def sle_poly_calculations(x_data, length, coefficents_tracked):
    return sum(coefficents_tracked[i] * x_data**i for i in range(length))

# - Behavior mods -
developer_mode = 1
chart_fabrication = 1
# -----------------
# ----> SLE section <----
if developer_mode == 1:
    print("SLE section pre dense initiated")

x_points = np.array([0,1,2,3,4,5])
y_points = np.array([0, 0.5, 0.7, 0.9, 1.2, 1.5])
if len(x_points) != len(y_points):
    print(f"Length of x points: {len(x_points)} | Length of y points: {y_points}")

n = len(x_points)
A = np.vander(x_points, increasing=True)
coefficients = solve(A, y_points)

lagrange_poly = lagrange(x_points, y_points)
x_fine = np.linspace(min(x_points), max(x_points), 300)
y_sle = [sle_poly_calculations(x_data=x_points,length=n, coefficents_tracked=coefficients) for x in x_fine]
y_lagrange = lagrange_poly(x_fine)
if developer_mode == 1:
    print("SPE section pre-dense protocols completed")
# ----> End of SLE section <----

# ----> Application of dense points <----
dense_x_points = np.arange(0, 5, 0.5)
dense_y_points = np.array([0, 0.3, 0.6, 0.8, 1.0, 1.1, 1.3, 1.4, 1.5, 1.6])
if len(dense_x_points) != len(dense_y_points):
    print(f"Length of x points: {len(dense_x_points)} | Length of y points: {len(dense_y_points)}")
# Dense conversions
n_dense_cnt = len(dense_x_points)
a_dense = np.vander(dense_x_points, increasing=True)
# Lagrange dense conversion
lagrange_dense_poly = lagrange(dense_x_points, dense_y_points)

# SLE and lagrange dense processing
dense_coefficients = solve(a_dense, dense_y_points)
sle_dense_var = sum(dense_coefficients[i] * x_fine**i for i in range(n_dense_cnt))
if developer_mode == 1:
    print("SPE section post-dense protocols completed")
# ----> End of application of dense points <----

# ----> Chart fabrication <----
if chart_fabrication == 1:
    # ---> SLE charting non-dense <---
    plt.figure(figsize=(8, 6))
    plt.plot(x_fine, y_sle, 'r--', label='SLE Interpolation')
    plt.plot(x_fine, y_lagrange, 'b-.', label='Lagrange Interpolation')
    plt.scatter(x_points, y_points, color='black', zorder=3, label='Interpolation Points')

    plt.legend()
    plt.title("Interpolation on [0,4]")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.tight_layout()
    plt.show()
    plt.close()
    # ---> SLE charting post dense conversion <---
    plt.figure(figsize=(8, 6))
    plt.plot(x_fine, sle_dense_var, 'r--', label='SLE Dense Interpolation')
    plt.plot(x_fine, lagrange_dense_poly(x_fine), 'b-.', label='Lagrange Dense Interpolation')
    plt.scatter(dense_x_points, dense_y_points, color='black', zorder=3, label='Interpolation Points (Dense)')
    plt.legend()
    plt.title("Interpolation with Dense Points")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.tight_layout()
    plt.show()

