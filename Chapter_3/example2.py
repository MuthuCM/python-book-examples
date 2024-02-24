# Example 3.2
# Program to find nth root using a Function
# Function to find nth root
def nthRoot(x,n):
  return x ** (1/n)
# Main Code
x = int(input("Type the value of x: "))
n = int(input("Type the value of n: "))

root = nthRoot(x,n)
print(f"{n}th root of {x} is: {root}")