# Example 1.3
# Dollar to Rupee conversion Version 2
dollars = int(input(" Type Amount in Dollars: "))
conversion_rate = float(input("Type Conversion Rate: "))
rupees = conversion_rate * dollars
print(f"$ {dollars}  = Rs. {rupees:8.2f}")