from Accounts.Account import Accounts

class Customers:
    def __init__(self, firstname, lastname):
        self.firstname=firstname
        self.lastname=lastname
        self.account=Accounts
    def getFirstname(self):
        return self.firstname
    def getLastname(self):
        return self.lastname
    def getName(self):
        return str(self.firstname +" "+ self.lastname)
    def setAccount(self, x):
        self.account=x
    def getAccount(self):
        return self.account.getBalance()
    def acc(self):
        return self.account



