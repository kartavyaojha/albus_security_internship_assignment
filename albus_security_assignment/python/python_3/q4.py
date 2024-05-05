class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return True
        else:
            print("Invalid deposit amount")
            return False

    def withdraw(self, amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            return True
        else:
            print("Invalid withdrawal amount")
            return False

    def check_balance(self):
        return self.balance


account = BankAccount()

account.deposit(100)
print("Balance:",account.check_balance())

account.withdraw(50)
print("Balance:",account.check_balance())

account.withdraw(60)
print("Balance:",account.check_balance())