# Example 4.5 - Version 2
# Program to draw Scatter Plot
# Import Libraries
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
# Specify Data
x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)
# Draw a Scatter Diagram
plt.scatter(x, y, c = colors, s = sizes, alpha = 0.9, cmap = 'viridis', marker = 'o')
plt.show()