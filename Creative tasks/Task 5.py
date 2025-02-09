import numpy as np


def heuristic_bijection(function, x1, x2, tolerance):
    if function(x1) * function(x2) >= 0:
        print("Bijection method requires the function to have different signs at the end points of and b")
        return None
    documented_intermediates = []
    c = x1
    while (x2 - x1)/2 > tolerance:
        c = (x1 + x2) / 2
        if function(c) == 0:
            print("Root detected")
            break
        elif function(x1) * function(x2) < 0:
            x2 = c
            documented_intermediates.append(x2)
        else:
            x1 = c
            documented_intermediates.append(x1)
    # Return
    return c, documented_intermediates[:-1]

function_applied = lambda x: x**4 + 3*x**3 + x**2 - 2*x - 0.5
lower = 0
upper = 3
tolerance = 0.01

values = []
x_axis = np.linspace(lower, upper, 200)
for i in x_axis:
    result = function_applied(i)
    values.append(result)

root_found, intermediates = heuristic_bijection(function_applied, lower, upper, tolerance)
print(f"Root found: {root_found}")
print(f"Intermediate roots: {intermediates}")
