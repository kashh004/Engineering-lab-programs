# 2D plots for Polar curves (r = 1 + cos(theta))
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 400)
r = 1 + np.cos(theta)
plt.polar(theta, r)
plt.title('Polar Plot: r = 1 + cos(theta)')
plt.show()
