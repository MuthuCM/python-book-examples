# Example 4.6 
# Line Plot using Seaborn
# Import Libraries
#%matplotlib inline
import seaborn as sns
# Specify Data
year = [1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960]
no_of_passengers = [1520,1676,2042,2364,2700,2867,3408,3939,4421,4572,5140,5714]
# Create Line Plot
sns.lineplot(x = year, y = no_of_passengers, color = 'r')
plt.title("Passenger Growth")
plt.xlabel("Year")
plt.ylabel("No. of Passengers ")
plt.show()