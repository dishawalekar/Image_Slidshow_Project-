
#Encapsulation concept
class BankAccount:
    def __init__(self,name,balance):
      self.name=name
      self.__balance=balance #private varible


    def deposit(self,amount):
       if amount> 0:
        self.__balance+= amount 

    def withdraw(self,amount):
       if 0< amount <=self.__balance:  
        self.__balance-= amount 

       else:
          print("Invalid withdraw")  

    def get_balance(self):
        return self.__balance     
      

acc1=BankAccount("Disha",10000)    
print("1st ",acc1.get_balance())
acc1.deposit(5000)
print("After",acc1.get_balance())
acc1.withdraw(2000)
print("after",acc1.get_balance())   
    