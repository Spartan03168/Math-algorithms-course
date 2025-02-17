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
