# Example 3.3
# Program to generate random numbers using a Function
# Function to generate random numbers in a given range
import random
def randomInRange(x,y):
  return random.randrange(x,y)
# Main Code
x = int(input("Type the first number of range: "))
y = int(input("Type the last number of range: "))
for i in range(0,3):
  print(randomInRange(x,y))