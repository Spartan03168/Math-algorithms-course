import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**4 + 3*x**3 + x**2 - 2*x - 0.5

def bijection(a, b):
    test_mode = 1
    if f(a) * f(b) >= 0:
        print("You have not assumed right a and b")
        return
    c = a
    tracked_intervalues = []

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
    return c, cycle, tracked_intervalues

x1 = -2
x2 = 3
# Bijection calculations: (a+b)/2
x_axis_data = np.linspace(x1, x2, num=100)
bijection_tracked, cycles, tracked_intermediates = bijection(x1, x2)
f_x = f(x_axis_data)
print("Bijection root",bijection_tracked,",", cycles,"cycles")
print(f"Tracked intermediates: {tracked_intermediates}")

"""
# -> Charting the results <-
plt.figure(figsize=(8,6))
plt.plot(x_axis_data, f_x, label="f(x)", color="blue")
plt.scatter(tracked_intermediates, f(np.array(tracked_intermediates)), color="green", s=100, label="Intermediates")
plt.axhline(0, color="red", linestyle="--")
plt.xlabel(f"Line space between {x1} and {x2}")
plt.ylabel("f(x)")
plt.title("Bijection method visualization")
plt.legend()
plt.tight_layout()
plt.show()
plt.close()
"""
