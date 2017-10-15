class Accounts:
    def __init__(self,balance=0):
        self.balance=balance
        self.balance=float()
    def getBalance(self):
        return '%.2f' % self.balance
    def deposit(self,amt):
        if amt > 0:
            self.balance+=amt
    def withdraw(self,amt):
        if self.balance >= amt:
            self.balance -= amt

