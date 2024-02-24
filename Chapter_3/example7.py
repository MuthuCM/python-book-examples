# Example 3.7
# Program to calculate mean and standard deviation using a Function
# Function to calculate mean and standard deviation
import math
def mean_and_sd(data):
  mean = sum(data)/len(data)
  sum_of_squares = 0
  for i in range(0,len(data)):
    sum_of_squares = sum_of_squares + (data[i] - mean) ** 2
  var = sum_of_squares/len(data)
  std_deviation =  math.sqrt(var)
  return mean , std_deviation
# Main code
values = list(eval(input("Type a list of values: ")))
average, sd = mean_and_sd(values)
print(f"Average = {average}")
print(f"Standard Deviation = {sd}")