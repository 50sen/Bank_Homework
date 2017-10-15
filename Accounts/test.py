from Accounts.Bank import Customers,Bank
from Accounts.Account import Accounts
c1=Customers("t","r")
bank=Bank("bank")
a1=Accounts()
c1.setAccount(a1)
bank.addCustomer(c1)
c1.acc().deposit(100)
print(bank.getCustomer().getAccount())
bank.getCustomer().acc().deposit(100)
print(bank.getCustomer().getAccount())
