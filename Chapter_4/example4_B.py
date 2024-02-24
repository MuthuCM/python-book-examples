# Example 4.4 - Version 2
# Program to draw Histogram
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
values = np.random.randn(1000)
plt.hist(values, bins = 40, density = True, alpha = 0.3,
         histtype = 'stepfilled',color = 'steelblue', edgecolor = 'none')
plt.show()