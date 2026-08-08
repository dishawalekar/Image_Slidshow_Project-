#inheritances
#Polymorphnism
class payment:
   def __init__(self,amount):
      self.amount=amount

   def pay(self):
      print("Payment is proceossing:",self.amount)  

class Creadicard(payment):
   def pay(self):
      print("Credit Card Payment of:",self.amount,"+3% pf ")

class UPIPayment(payment):
   def pay(self):
       
        print("UPI Payment of:",self.amount,"no free  ")


p1=Creadicard(500)
p1.pay()

p2=UPIPayment(100)
p2.pay()