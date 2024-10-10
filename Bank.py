# create Account
# view acc details by acc no
# withdraw
# deposit
# fund transfer
# print transactions
# exit
# type: ignore
class Account:
    customers={}
    def __init__(self,acc_no,name,dob,phno,city):
        self.bal=0
        self.transactions=[]
        self.acc_no=acc_no
        self.name=name
        self.phno=phno
        self.dob=dob
        self.city=city
        Account.customers[self.acc_no]=[self.name,self.dob,self.phno,self.city,self.bal]
    def createAccount(self):
        print("Account created successfully")
    @staticmethod
    def getDetails(acc):
        found=False
        for i in Account.customers:
            if i==acc:
                found=True
        if(found):
            print("-----------PERSONAL DETAILS----------------")
            print("Name:",Account.customers[acc][0])
            print("Account Number:",acc)
            print("DOB:",Account.customers[acc][1])
            print("City:",Account.customers[acc][3])
            print("Phone Number:",Account.customers[acc][2])
            print("Available Balance:",Account.customers[acc][-1])
            print("-------------------------------------------")
        else:
            print("Invalid account number")
            print("-------------------------------------------")
    def getBalance(self):
        print("---------BALANCE--------------")
        print("Name:",self.name)
        print("Available Balance:",self.bal)
    def withdraw(self,amount):
        if(self.bal>=amount):
            self.bal-=amount
            Account.customers[self.acc_no][-1]-=amount
            print("Withdrawn Amount:",amount)
            print("Available balance:",self.bal)
            self.transactions.append(["withdraw",amount])
            print("-------------------------------------------")
        else:
            print("Insufficient funds")
            print("-------------------------------------------")
    def deposit(self,amount):
        self.bal+=amount
        Account.customers[self.acc_no][-1]+=amount
        print("Deposited Amount:",amount)
        print("Available balance:",self.bal)
        self.transactions.append(["deposit",amount])
        print("-------------------------------------------")
    def fundTransfer(self,acc,amount):
        if(self.bal>=amount):
            self.bal-=amount
            for i in Account.customers.keys():
                if i==acc:
                    Account.customers[acc][-1]+=amount 
                    Account.customers[self.acc_no][-1]-=amount
                    print("Fund transfer of",amount,"successful to",Account.customers[acc][0])
                    print("Available balance:",self.bal)
                    self.transactions.append(["fund transfer",amount])
                    print("-------------------------------------------")
                else:
                    print("Invalid account number")
        else:
            print("Insufficient funds")
            print("-------------------------------------------")
    def getTransactions(self):
        print("Transactions:")
        for i in self.transactions:
            print(*i)
        print("-------------------------------------------")
a=Account(12345678,"abc","01-01-2003",123,"New York")
s=Account(23456789,"xyz","01-01-2002",987,"Paris")
while(True):
    c=int(input("Bank services:\n1.Deposit\n2.Withdraw\n3.Fund Transfer\n4.Balance Enquiry\n5.Transaction history\n6.Account Details\n7.Exit\nEnter option: "))
    if(c==1):
        amount=int(input("Enter amount to deposit: "))
        a.deposit(amount)
    elif(c==2):
        amount=int(input("Enter amount to withdraw: "))
        a.withdraw(amount)
    elif(c==3):
        amount=int(input("Enter amount to transfer: "))
        a.fundTransfer(23456789,amount)
    elif(c==4):
        a.getBalance()
    elif(c==5):
        a.getTransactions()
    elif(c==6):
        Account.getDetails(12345678)
    else:
        break