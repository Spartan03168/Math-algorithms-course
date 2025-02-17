"""
Natural cubic spline code
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline, interp1d

x = np.arange(2,20)
y = 1/(x)
# - Cubic spline interpolation -
cube_spline = CubicSpline(x, y, extrapolate=True)
# - Natural cubic spline interpolation -
natural_spline = CubicSpline(x, y, bc_type="natural", extrapolate=True)
# - Apply linear interpolation -
linear_int = interp1d(x,y)

xs = np.arange(2, 9, 0.1)
ys = linear_int(xs)

# - Plot linear interpolation -
plt.plot(x, y,'o', label='data')
plt.plot(xs,ys,  label="interpolation", color='green')
plt.legend(loc='upper right', ncol=2)
plt.title('Linear Interpolation')
plt.show()

# - Define a new xs -
xs = np.arange(1,15)
# - Plot cubic spline and natural cubic spline -
plt.plot(x, y, 'o', label='data')
plt.plot(xs, 1/(xs), label='true')
plt.plot(xs, cube_spline(xs), label="S")
plt.plot(xs, natural_spline(xs), label="NS")
plt.plot(xs, natural_spline(xs,2), label="NS''")
plt.plot(xs, natural_spline(xs,1), label="NS'")
plt.legend(loc='upper right', ncol=2)
plt.title('Cubic/Natural Cubic Spline Interpolation')
plt.show()

print("Value of double differentiation at boundary conditions are %s and %s"%(natural_spline(2,2),natural_spline
(10,2)))