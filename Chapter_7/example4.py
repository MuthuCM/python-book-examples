# Exercise 7.4
# Function to find factorial of a number
def factorial(n):
  value = 1
  for i in range(1 , n+1):
    value = value * i
  return value
# Function to find n c r and n p r values
def ncrnpr(n,r):
  ncr_value = factorial(n)/(factorial(r)*factorial(n-r))
  npr_value = factorial(n)/factorial(n-r)
  return ncr_value, npr_value
# Code to find n c r and n p r using the above function
n = eval(input("Type the value of N: "))
r = eval(input("Type the value of R: "))
ncr_value, npr_value = ncrnpr(n,r)
print(f"Value of {n} c {r} = {ncr_value} ")
print(f"Value of {n} p {r} = {npr_value} ")