# Example 5.9
# Program to calculate Mean and SD using List Comprehension
import math
data = list(eval(input('Type the 5 values: ')))
print (data)
# Mean of data
mean = sum(data)/len(data)
print(f"Mean = {mean}")
# Square Deviations - List Comprehension
deviations = [(x - mean) ** 2 for x in data]
# Variance
var = sum(deviations)/len(data)
print(f"Variance = {var}")
std_deviation =  math.sqrt(var)
print(f"Std. Deviation = {std_deviation:8.2f}")