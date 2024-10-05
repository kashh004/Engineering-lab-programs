# 2D plots for Cartesian curves (y = x^2)
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
y = x**2
plt.plot(x, y)
plt.title('Cartesian Plot: y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
