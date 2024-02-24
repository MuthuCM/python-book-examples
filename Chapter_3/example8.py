# Example 3.8
# Program to calculate compound interest
# Function to calculate compound interest
def compound_interest(p,n,r = 10):  # Default Parameter
  return (p*(1+(r/100))**n) - p
# Main Code
customer_type = input(" Cutomer Type(HNI/Others): ")
if customer_type == "HNI":
  principal     = int(input(" Type Principal: "))
  years         = int(input(" Type Period of Deposit: "))
  interest_rate = float(input(" Type Interest Rate: "))
  interest	= compound_interest(principal,years,interest_rate)
else:
  principal     = int(input(" Type Principal: "))
  years         = int(input(" Type Period of Deposit: "))
  interest	= compound_interest(principal,years)

print(f"Compound Interest = Rs. {interest:8.2f}")