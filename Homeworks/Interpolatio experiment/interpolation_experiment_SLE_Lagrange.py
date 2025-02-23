import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy.linalg import solve

# ----> Functions <----
def gauss_seidel_iteration(A, b, x0, x_exact, tolerance, iterations):
    n = len(b)
    x = x0.copy()
    errors = []
    for it in range(iterations):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - s) / A[i][i]
            error = np.linalg.norm(x - x_exact)
            errors.append(error)
            if error < tolerance:
                break
        return x, errors

def gen_initial_x0(x_exact,n):
    x0 = x_exact + np.random.uniform(-0.5, 0.5, n)
    return x0

def create_diag_dominant_matrix(n):
    A = np.random.rand(n, n)
    for i in range(n):
        A[i, i] = sum(np.abs(A[i])) + np.random.rand()
    return A

def jacobi_iteration_first(A, b, x0, iterations):
    n = len(b)
    x = x0
    for it in range(iterations):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
            x = x_new
            print(f"Iteration {it+1}: {x}")
    return x

def jacorbi_method(A, b, x0, x_exact, tolerance, iterations):
    n = len(b)
    x = x0
    errors = []
    for it in range(iterations):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
            x = x_new
            error = np.linalg.norm(x - x_exact)
            errors.append(error)
            if error < tolerance:
                break
        return x, errors

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

# ---> Deployment <---
dev_mode = 1
chart_fab_key = 1
tolerance=1e-5

x_points = np.linspace(0, 4, 6)
sin_func_1_sle_poly, sin_func_1_lagrange_poly, sin_func_1_y_lagrange = interpolation_process(np.sin, x_points, "Interpolation of sin(x) on [0,4]", chart_fabrication=chart_fab_key, developer_mode=dev_mode)
sin_func_2_sle_poly, sin_func_2_lagrange_poly, sin_func_2_y_lagrange = interpolation_process(lambda x: np.sin(3 * x), x_points, "Interpolation of sin(3x) on [0,4]", chart_fabrication=chart_fab_key, developer_mode=dev_mode)
sin_func_3_sle_poly, sin_func_3_lagrange_poly, sin_func_3_y_lagrange = interpolation_process(lambda x: np.sin(5 * x), x_points, "Interpolation of sin(5x) on [0,4]", chart_fabrication=chart_fab_key, developer_mode=dev_mode)

# Jacorbi deployment
iteration_lock = 10
n = 3
A_01 = create_diag_dominant_matrix(n)
x_exact_01 = np.random.rand(n)
b_vector_01 = np.dot(A_01, x_exact_01)
x0_01 = gen_initial_x0(x_exact_01, n)
if dev_mode == 1:
    print(f"Matrix A:\n{A_01}")
    print(f"\nKnown solution x_exact:\n{x_exact_01}")
    print(f"\nRight-hand side b:\n{b_vector_01}")
    print(f"\nInitial approximation x0:\n{x0_01}")

solution = jacobi_iteration_first(A_01, b_vector_01, x0_01, iterations=iteration_lock)
xj, jacobi_errors = jacorbi_method(A=A_01, b=b_vector_01, x0=x0_01, tolerance=tolerance, x_exact=x_exact_01, iterations=50)
print(f"\nJacobi solution: \n{solution}")
print(f"\nExact Solution x:\n{x_exact_01}")

# ---- Gauss seidel deployment ----
A_02 = create_diag_dominant_matrix(n)
x_exact_02 = np.random.rand(n)
b_vector_02 = np.dot(A_02, x_exact_02)
x0_02=gen_initial_x0(x_exact_01,n)

gauss_solution = gauss_seidel_iteration(A=A_01,b=b_vector_02,x0=x0_02,x_exact=x_exact_02,tolerance=tolerance,iterations=iteration_lock)
xg, gauss_seidel_errors = gauss_seidel_iteration(A_02, b_vector_02, x0_02, x_exact=x_exact_02, tolerance=tolerance, iterations=50)
# ----> Plotting process <----
if chart_fab_key == 1:
    plt.plot(jacobi_errors, label='Jacobi')
    plt.plot(gauss_seidel_errors, label='Gauss-Seidel')
    #plt.yscale('log')
    plt.xlabel('Iteration')
    plt.ylabel('Error')
    plt.title('Convergence of Jacobi and Gauss-Seidel')
    plt.legend()
    plt.show()