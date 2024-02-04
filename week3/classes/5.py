class Account:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self):
        self.balance = self.balance + int(input())
        return self.balance
    def withdraw(self):
        self.balance = self.balance - int(input())
        return self.balance

pr = Account(100)
print(pr.withdraw())
print(pr.deposit())
print(pr.withdraw())
