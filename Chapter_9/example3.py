# Example 9.3
# Defining a class named "SavingsAccount"
class SavingsAccount:
  def __init__(self,name):
    self.name = name
    self.balance = 0.0
  def credit_money(self,amount):
    self.balance = self.balance + amount
    print(f"{self.name} deposited Rs. {amount}")
  def debit_money(self,amount):
    if amount > self.balance:
      print(f"Type an amount less than Rs. {self.balance}")
    else:
      self.balance = self.balance - amount
      print(f"{self.name} withdrew Rs. {amount}")
  def display_balance(self):
    print(f"{self.name} has a balance of Rs. {self.balance}")
# Object Creation
savings_account = SavingsAccount("Roshita")
savings_account.credit_money(10000)
savings_account.debit_money(6000)
savings_account.display_balance()