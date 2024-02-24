# Example 4.2
# Program to draw Bar Chart
# Import Libraries
import matplotlib.pyplot as plt
# %matplotlib inline
# Specify Data
movies = ["Annie Hall","Ben-Hur","Casablanca","Gandhi","WestSide Story"]
num_oscars = [5,11,3,8,10]
colors = ['b','g','r','c','m']
# Draw a Bar Chart
plt.bar(range(0,len(movies)),num_oscars, color = colors, align = 'center')
plt.title("My Favourite Movies")
plt.xlabel("Movie Name")
plt.ylabel("No. of Oscar Awards")
plt.xticks(range(0,len(movies)), movies)
plt.show()