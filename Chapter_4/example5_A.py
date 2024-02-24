# Example 4.5 
# Program to draw Scatter Plot
# Import Libraries
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
# Specify Data
x = [65, 66,67,67,68,69,70,72,64,67,66,68,67,70,69,73]
y = [67,68,65,68,72,72,69,71,66,69,64,69,71,73,68,72]
# Draw a Scatter Diagram
plt.scatter(x, y, marker = '*')
plt.show()