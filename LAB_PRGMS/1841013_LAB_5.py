class bank_acc: 
    def __init__(self): 
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 
  
    def dep(self): 
        amt=float(input("Enter amount to be Deposited: ")) 
        self.balance += amt 
        print("\n Amount Deposited:",amt) 
  
    def withdraw(self): 
        amt = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amt: 
            self.balance-=amt 
            print("\n You Withdrew:", amt) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 
  

   
#object creation of class 
s = bank_acc() 
   
# Calling functions with class object 
s.dep() 
s.withdraw() 
s.display() 