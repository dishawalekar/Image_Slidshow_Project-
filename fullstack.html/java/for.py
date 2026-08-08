#0 1 1 2 3 5
#class laptop:
 #   brand="default"
  ##
  #  price="1 lakh"
#laptop1=laptop()
#laptop1.brand="MAcbook"
#laptop1.RAM="64GB"
#print("Laptop 1 brand",laptop1.brand)
#print("Laptop 1 brand",laptop1.RAM)

#laptop2=laptop()
#laptop2.brand="DEll"
#laptop2.RAM="32GB"
#print("laptop2 brand",laptop2.brand)

"""class foodItem:
    category="xyz college"
    def __init__(self,name):
        self.name=name
        
f1=foodItem("Samosa")
f2=foodItem("gulabo")
print(f1.name)"""

"""class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark

    def average(self):  
        total=0
        for i in self.mark:
            total+=i
            avg=total/len(self.mark)

        print("Name of srudent:",s1.name) 
        print("Marks of Student",s1.mark)
        print("Average of Marks is:",avg)
s1=student("Disha",[98,67,90])
#s1=student("math:92","py:98")
s1.average()"""

#Print numbers 1 to 100. Multiples of 3 → "Fizz", multiples of 5 → "Buzz", both → "FizzBuzz".
        

"""for i in range(1,20):
   output=""
   if i % 3==0 :
          print("Fizz",i)
          output+="Fizz"
          if i % 5==0:
            print("Buzz",i)
            output+="Buzz"
print(output or i)   """

"""num=input("Enter the value:")
#if num == str(num):
n= num[::-1]
if num == str(num) and num == n:
      print("Palidrom number")
elif  num == n: 
    #n=num[::-1]
    print("palidrom number")     
        
else:
    print("not palidrom number")"""

"""num=int(input("Enetr the value"))
i=1
while i<=len(num):
 i=i+1
 n=i+len(num)
 print(n)"""

"""def factorial(x):
    if x == 1:
      return 1
    else:
        return(x*factorial(x-1))
num=int(input("Enter the number:"))
print(factorial(num)) """



"""def full_pyramid(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        
        for k in range(1, 2*i):
            print("*", end="")
        print()
   
full_pyramid(5)"""

"""for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print("")"""


#def half_pyramid(n):
"""for i in range(1, 5+ 1):
     for j in range(1, i + 1):
        print("* ", end="")
     print("")"""

#half_pyramid(5)

"""def print_diamond(rows):
    # Upper half of the diamond
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print("*" * (2 * i - 1))
        
    # Lower half of the diamond
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        print("*" * (2 * i - 1))

# Example usage:
print_diamond(5)"""

#from os import remove


"""lis=[1,2,3,4,5,6,4,3,2]
print(" remove duplicates in the lis without using set")

for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i]==lis[j]:
            print(lis.remove(lis[i]))
"""
"""n=int(input("enter the no of :"))
list=[]
for i in range(n):
   num=int(input("Enter the vlaue in list:"))
list.append(num)
largest= secound_lar = float('-inf')

for num in list:
    if num > largest:
        secound_lar=largest
        largest = num
    elif num > secound_lar and num != largest:
        secound_lar = num
print("secound largest is:",secound_lar)         

#f secound_lar == float('-inf'):
 #   print("Does not exit")
#else:
  #  print("secound lar is",secound_lar)    
"""

name="My name is disha I am from maharashtra"
for i in range(len(name)):
    i+=1
    n=i.count(name)
    
    print(n)
