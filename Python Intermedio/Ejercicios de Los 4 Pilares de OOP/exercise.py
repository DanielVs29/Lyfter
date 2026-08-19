
class BankAccount:
    balance = 0

    def add_balance(self, amount):
        self.balance += amount
        return self.balance

    def substract_balance(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance

class SavingsAccount(BankAccount):

    def __init__(self, min_balance):    
        self.min_balance = min_balance

    def substract_balance(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Balance cannot go below minimum balance")



cuenta = SavingsAccount(100)

cuenta.add_balance(500)

try:
    print(cuenta.substract_balance(300))
except ValueError as error:
    print(error)

try:
    print(cuenta.substract_balance(150))
except ValueError as error:
    print(error)

