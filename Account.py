""" Create a Account class with methods"""
 def __init__(self, balance=0.0, interest=0.0): 
        self.balance = balance
        self.interest = interes
 def set_balance(self,balance):
    self.balance = balancet def set_interest(self, interest):

    self.interest = interest
 def deposit(self, amount):          if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive." def withdraw(self, amount):
      if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance or invalid amount. def calculate_interest(self):
     return (self.balance * self.interest) / 100
 def display_account_info(self):
       print(f"Balance: ${self.balance:.2f}, Interest Rate: {self.interest}%")
"= interest
