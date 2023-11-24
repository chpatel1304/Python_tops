class BankDemo:

    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello ",self.cname,", Your Account Number ",self.acno," Is Opened With ",self.balance," Rs.")
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            self.needs=amount-self.balance
            print("Sorry You Need Another ",self.needs," Rs.")
    def checkBalance(self):
        print("Your Current Balance Is ",self.balance," Rs.")

acno=int(input("Enter Account Number : "))
cname=input("Enter Customer Name : ")
balance=int(input("Enter Initial Balance To Open Account : "))

b1=BankDemo()
b1.openAccount(acno,cname,balance)

while True:
    print("******************************************************")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("******************************************************")
    choice=int(input("Enter Your Choice : "))
    print("******************************************************")
    
    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("******************************************************")
    elif choice==2:
        amount=int(input("Enter Withdrawl Amount : "))
        b1.withdraw(amount)
        print("******************************************************")
    elif choice==3:
        b1.checkBalance()
        print("******************************************************")
    elif choice==4:
        print("Thank You For Using Our Services. Good Bye")
        print("******************************************************")
        break
    else:
        print("Invalid Choice")
         
