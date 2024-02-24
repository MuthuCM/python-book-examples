# Example 3.6
# Program to calculate compond interest using a Function
# Function to calculate compound interest
def compound_interest(p,n,r):
  return (p*(1+(r/100))**n) - p
# Main Code
principal     = int(input(" Type Principal: "))
years         = int(input(" Type Period of Deposit: "))
interest_rate = float(input(" Type Interest Rate: "))
interest	= compound_interest(principal,years,interest_rate)
print(f"Compound Interest = Rs. {interest:8.2f}")