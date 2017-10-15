from Accounts.Bank import Bank
from Accounts.Customer import Customers, Accounts

'''b1=Bank("Bank1")
c1=Customers("Russo", "T")
a1=Accounts(0)
c1.setAccount(a1)
print(c1.getAccount())
a1.deposit(1005)
print(c1.getAccount())
b1.addCustomer(c1)
print(b1.Customerlist())
'''
'''while True:
    identity = input("Enter your ID: \n")
    if identity == "812736128":
        x=input("What would you like to do: \nBalance Inquiry \nDeposit \nWithdraw \nTransfer \n").upper()
        try:
            if x == "BALANCE INQUIRY":
                print("Your balance is: \n", acc1.getbalance)
            elif x == "WITHDRAW":
                x=int(input("Input amount: \n"))
                acc1.withdraw(x)
                print(())
'''
bank=Bank("Iron Bank")
print("Welcome to the " + str(bank.getBankname()))
while True:
    print("What would you like to do:\n"
          "1. Create an Account\n"
          "2. View the customer list\n"
          "3. Do customer things\n"
          "4. Exit\n")
    choice=int(input())
    if choice==1:
        if len(bank.customerList)<1:
            firstname=input("input first name:")
            lastname=input("input last name:")
            c1=Customers(firstname,lastname)
            bank.addCustomer(c1)
            a1=Accounts()
            c1.setAccount(a1)
        else:
            print("bank is full")
    elif choice==2:
        print(bank.customerList)
    elif choice==3:
        if len(bank.customerList2)<1:
            print("no one here")
        else:
            while True:
                inp=int(input("1.check balance\n2.deposit\n3.withdraw\n4.return\n"))
                if inp==1:
                    print("your balance is: "+ bank.getCustomer().getAccount())
                elif inp==2:
                    amt=float(input("input amount:\n"))
                    bank.getCustomer().acc().deposit(amt)
                    print("balance is now:\n", bank.getCustomer().getAccount())
                elif inp==3:
                    amt=float(input("input amount:\n"))
                    bank.getCustomer().acc().withdraw(amt)
                    print("balance is now:\n", bank.getCustomer().getAccount())
                elif inp==4:
                    break
    elif choice==4:
        print("thank you for coming")
        exit()
    else:
        print("invalid input")





