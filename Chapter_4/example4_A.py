# Example 4.4 
# Program to draw Histogram
# Import Libraries
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
# Specify Data
values = [44,6,35,23,11,4,35,27,19,13,21,32,17,
          29,38,33,14,25,37,15,25,22,28,24,26,47]
# Draw a Histogram
plt.hist(values , bins = 5)
plt.show()