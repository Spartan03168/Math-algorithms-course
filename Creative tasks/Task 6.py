# Parametric function circle
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 75)
r = -16 * (np.sin(theta)**3)

plt.figure(figsize=(7, 7))
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, color='blue', linewidth=2)

ax.set_title(r'$16 \sin^3(\theta)$', fontsize=16, fontweight='bold')
plt.show()