# Example 4.1 
# Program to draw Line Chart
# Import Libraries
import matplotlib.pyplot as plt
# %matplotlib inline
# Specify Data
years = [1960,1970,1980,1990,2000,2010,2020]
gdp = [300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]
# Draw a Line Chart
plt.plot(years, gdp, color = 'blue', marker = 'o', linestyle = 'solid')
plt.title("GDP Growth")
plt.xlabel("Year")
plt.ylabel("GDP in Billions ")
plt.show()