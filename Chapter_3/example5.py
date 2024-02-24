# Example 3.5
# Program to calculate simple interest using a Function
# Function to calculate simple interest
def simple_interest(p,n,r):
  return (p*n*r)/100
# Main Code
principal     = int(input(" Type Principal: "))
years         = int(input(" Type Period of Deposit: "))
interest_rate = float(input(" Type Interest Rate: "))
interest	= simple_interest(principal,years,interest_rate)
print(f"Simple Interest = Rs. {interest:8.2f}")
