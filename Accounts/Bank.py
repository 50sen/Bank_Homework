from Accounts.Customer import Customers
class Bank:
    def __init__(self,bankname):
        self.bankname=bankname
        self.customerList=[]
        self.numCustomers=int()
        self.customerList2=[]
    def addCustomer(self,x):
        self.customer=x
        self.customerList.append(x.getName())
        self.customerList2.append(x)
    def getNumCustomers(self):
        return len(self.customerList)
    def getCustomer(self):

        return self.customerList2[-1]
    def Customerlist(self):
        for i in self.customerList:
            print(i)
    def getBankname(self):
        return self.bankname

