from Converters import numpy_conversion, list_conversion
from Functionalities import points_file_reader, legrange_interpolation, parametric_interpolation

print("Interpolation multitool")
cleared_choices = ["Function", "File"]
choice = input("Choose input method (1: Function, 2: File): ")
while choice not in cleared_choices:
    choice = input(f"Try again. Use these cleared choices {cleared_choices}: ")

if choice == "Function":
    pass
elif choice == "File":
    pass