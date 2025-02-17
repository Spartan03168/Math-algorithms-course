from Converters import numpy_conversion, list_conversion
from Functionalities import points_file_reader, legrange_interpolation, parametric_interpolation
from sympy import sympify, Symbol
import numpy as np

print("Interpolation multitool")
cleared_choices = ["Function", "File"]
choice = input("Choose input method (1: Function, 2: File): ")
while choice not in cleared_choices:
    choice = input(f"Try again. Use these cleared choices {cleared_choices}: ")

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
