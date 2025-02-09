import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt

def fixed_point_iteration(g, x0, tolerance, iterations_cnt):
    x = x0
    iterations = []
    values = []

    for elements in range(iterations_cnt):
        x_next = g(x)
        iterations.append(elements)
        values.append(x)
        if abs(x_next - x) < tolerance:
            return x_next, elements + 1, iterations, values
        x = x_next

    print("Failure to converge")
    return None, iterations_cnt, iterations, values

def g1(x):
    return np.cos(x)

def g2(x):
    return (x + np.sin(x)) / 2

def g3(x):
    return np.sqrt(1+x)

start_time = datetime.datetime.now()
# -> Test case <-
tolerance = 1e-6
iterations = 40000
x1 = 0.5

# -> Fixed point iteration <-
print(f"Iterations available: {iterations}")
print("Fixed point iteration in progress\n")
print("First test in progress")
root_g1, iter_g1, iter_list_g1, values_g1 = fixed_point_iteration(g1, x1, tolerance, iterations_cnt=iterations)
print("Second test in progress")
root_g2, iter_g2, iter_list_g2, values_g2 = fixed_point_iteration(g2, x1, tolerance, iterations_cnt=iterations)
print("Third test in progress")
root_g3, iter_g3, iter_list_g3, values_g3 = fixed_point_iteration(g3, x1, tolerance, iterations_cnt=iterations)

print(f"\nRoot for g1(x) approximates {root_g1} after {iter_g1} iterations")
print(f"Root for g2(x) approximates {root_g2} after {iter_g2} iterations")
print(f"Root for g3(x) approximates {root_g3} after {iter_g3} iterations")

end_time = datetime.datetime.now() - start_time
print(f"End time: {end_time}")
# -> Charting process <-