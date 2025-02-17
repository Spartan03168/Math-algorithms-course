from Converters import numpy_conversion, list_conversion
from Functionalities import points_file_reader, legrange_interpolation, parametric_interpolation, sle_interpolation
from sympy import sympify, Symbol
import numpy as np
import matplotlib.pyplot as plt

print("Interpolation multitool")
cleared_choices = ["Function", "File"]
choice = input("Choose input method (1: Function, 2: File): ")
while choice not in cleared_choices:
    choice = input(f"Try again. Use these cleared choices {cleared_choices}: ")

# - Selection shell -
points = None
if choice == "Function":
    # -> Input section <-
    function_expression = input("Function applied: ")
    a, b = map(float, input("Enter interval [a, b]: ").split())
    degrees = int(input("Enter polynomial degree: "))
    # -> Processing <-
    function = sympify(function_expression)
    x_vals = np.linspace(a, b, degrees + 1)
    points = np.array([[x, function.evalf(subs={Symbol('x'): x})] for x in x_vals])
elif choice == "File":
    # -> Input section <-
    file_name = input("Enter file path: ")
    # -> Processing <-
    points = points_file_reader(file_name)

# -> Deployment <-
methods = {}
if input("Cleared for lagrange interpolation? (Cleared/Disable): ").lower() == "Cleared":
    methods['Lagrange'] = legrange_interpolation(points, x_val=None)[0]
if input("Cleared for parametric interpolation? (Cleared/Disable): ").lower() == "Cleared":
    methods['Parametric'] = parametric_interpolation(points, x_val=None)
if input("Cleared for SLE interpolation? (Cleared/Disable): ").lower() == "Cleared":
    methods['SLE'] = sle_interpolation(points, x_val=None)[0]

plt.scatter(points[:, 0], points[:, 1], color='red', label='Data points')
x_range = np.linspace(min(points[:, 0]), max(points[:, 0]), 500)
for name, poly in methods.items():
    if name == 'Parametric':
        t_vals = np.linspace(0, 1, 500)
        x_vals = [poly[0][0].evalf(subs={Symbol('t'): t}) for t in t_vals]
        y_vals = [poly[1][0].evalf(subs={Symbol('t'): t}) for t in t_vals]
    else:
        x_vals = x_range
        y_vals = [poly.evalf(subs={Symbol('x'): x}) for x in x_range]
    plt.plot(x_vals, y_vals, label=name)
plt.legend()
plt.show()

while True:
    val = input("Calculate polynomial value at x (press enter to quit): ")
    if not val:
        break
    x_val = float(val)
    for name, poly in methods.items():
        if name == 'Parametric':
            t_val = x_val
            result = (poly[0][0].evalf(subs={Symbol('t'): t_val}), poly[1][0].evalf(subs={Symbol('t'): t_val}))
        else:
            result = poly.evalf(subs={Symbol('x'): x_val})
        print(f"{name} interpolation at x={x_val}: {result}")