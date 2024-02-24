# Example 1.4
# Program to calculate Simple Interest
# Input Part
principal     = int(input(" Type Principal: "))
years         = int(input(" Type Period of Deposit: "))
interest_rate = float(input(" Type Interest Rate: "))
#Calculation Part
simple_interest	= (principal * years * interest_rate) / 100
#Output Part
print(f"Simple Interest = Rs. {simple_interest:8.2f}")