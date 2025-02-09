import numpy as np
import datetime
import matplotlib.pyplot as plt

def f(x):
    return (x - 1)**3

def df(x):
    return 3*(x-1)**2

def bijection(a, b, tolerance, max_iterations):
    test_mode = 1
    if f(a) * f(b) >= 0:
        print("You have not assumed right a and b")
        return
    c = a
    tracked_intervalues = []

    # --- Error tracker ---
    errors_documented = []
    for i in range(max_iterations):
        c = (a + b) / 2
        error = abs(b - a) / 2
        errors_documented.append(error)
        if error < tolerance or f(c) == 0:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    # --- Root tracker ---
    while (b - a) >= 0.01:
        # Find middle point
        c = (a + b) / 2
        # Check if middle point is root
        if f(c) == 0.0:
            break
        # Decide the side to repeat the steps
        if f(c) * f(a) < 0:
            b = c
            if test_mode == 1:
                tracked_intervalues.append(b)
        else:
            a = c
            if test_mode == 1:
                tracked_intervalues.append(a)

    cycle = len(tracked_intervalues)
    # Return
    return c, cycle, tracked_intervalues, errors_documented

def newtons_algo(f, df, x_0, tolerance, max_iterations, diagnostic_mode):
    x = x_0
    errors_tracked = []
    if diagnostic_mode == 1:
        if len(errors_tracked) > 0:
            print(f"-------\nErrors accumulated: {len(errors_tracked)}")
            print(">-<")
            for error in range(len(errors_tracked)):
                print(f"Error {error + 1}: {errors_tracked[error]}")
            print(">-<\n-------")

    for i in range(max_iterations):
        updated_x = x - f(x) / df(x)
        error_found = abs(updated_x - x)
        errors_tracked.append(error_found)
        # -> Breaker <-
        if error_found < tolerance:
            break
        x = updated_x

    return errors_tracked

def fixed_point_iteration(x0, tolerance, alpha, iterations_cnt):
    x = x0
    iterations = []
    values = []
    errors = []
    for elements in range(iterations_cnt):
        x_next = x - alpha * f(x)
        error_tracked = abs(x_next - x)
        # --- List updating ---
        errors.append(error_tracked)
        iterations.append(elements)
        values.append(x)
        # --- End stage ---
        if abs(x_next - x) < tolerance:
            return x_next, elements + 1, iterations, values, errors
        x = x_next
    # --- Failsafe ---
    print("Failure to converge")
    return None, iterations_cnt, iterations, values, errors

# - Behavior mods -
diagnostic_mode = 0

# Testing platform deployment
x_0 = 0.5
a = -2
b = 2
alpha = 0.5
tolerance = 1e-6
iteration = 150

# Newtons algo, bisection, fixed point
start_time = datetime.datetime.now()
print("----")
newton_errors_identified = newtons_algo(f, df, x_0, tolerance, max_iterations=iteration, diagnostic_mode=diagnostic_mode)
print("Newtons algorithm")
print(f"Newtons algo errors tracked:\n{newton_errors_identified}")
print("----")
c, cycles, tracked_intervals, bijection_errors = bijection(a, b, tolerance, max_iterations=iteration)
print("Bijection algorithm")
print(f"c: {c}\nCycles: {cycles}\nIntervals: {tracked_intervals}")
print("----")
x, element_count, iterations, values, errors = fixed_point_iteration(x0=x_0, tolerance=tolerance, iterations_cnt=iteration, alpha=alpha)
print("Fixed point iteration")
print(f"x:\n{x}")
print(f"Element count:\n{element_count}")
print(f"Iterations:\n{iterations}")
print(f"Values:\n{values}")
print(f"Errors:\n{errors}")
print("----")
end_time = datetime.datetime.now() - start_time
print(f"Processing time: {end_time}")

# --- Charting process ---
plt.figure(figsize=(8, 6))
plt.plot(range(1, len(newton_errors_identified) + 1), newton_errors_identified, label="Newton's Method", marker='o')
plt.plot(range(1, len(bijection_errors) + 1), bijection_errors, label="Bisection Method", marker='s')
plt.plot(range(1, len(errors) + 1), errors, label="Fixed Point Iteration", marker='^')
plt.yscale('log')
plt.xlabel("Iteration")
plt.ylabel("Error (log scale)")
plt.title("Convergence of Root Finding Methods")
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()
plt.close()