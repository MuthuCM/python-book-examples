# Example 5.6
# Program to calculate Mean and SD
import math
data = list(eval(input('Type the 5 values: ')))
print (data)
# Mean of data
mean = sum(data)/len(data)
print(f"Mean = {mean}")
# Sum of Squares of Deviations
sum_of_squares = 0
for i in range(0,len(data)):
  sum_of_squares = sum_of_squares + (data[i] - mean) ** 2
# Variance
var = sum_of_squares/len(data)
print(f"Variance = {var}")
std_deviation =  math.sqrt(var)
print(f"Std. Deviation = {std_deviation:8.2f}")