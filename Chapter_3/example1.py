# Example 3.1 
# Program to find n c r value
# Function to calculate factorial
def factorial(n):
  value = 1
  for i in range(1 , n+1):
    value = value * i
  return value
# Main Code
n = int(input("Type the value of N: "))
r = int(input("Type the value of R: "))
ncr_value = factorial(n)/(factorial(n-r)*factorial(r))
print(f"Value of {n} c {r} = {ncr_value} ")
