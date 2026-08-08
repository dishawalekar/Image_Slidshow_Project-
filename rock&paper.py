import random

item=["Rock","Paper","Scissors"] 

user_choice=input("Enter your choice(Rock,Paper,Scissors):"). lower()
computer_choice=random.choice(item)

#if user_choice not in item:
   # print("Invalid choice. Please enter Rock, Paper, or Scissors.")
#else:
print(f"User choice:{user_choice}  Computer choice:{computer_choice}") 

if user_choice == computer_choice:
      print("It is tie!")

elif user_choice == "Rock" :
    if computer_choice == "Paper": 
        print("computer Wins") 

    else:
        print("User Wins") 

elif user_choice == "Paper":
    if computer_choice == "Scissors":
        print("computer Wins")  

    else:
        print("user Wins")  
  

elif user_choice == "Scissors":
    if computer_choice == "Paper":
        print("user Wins")
    else:
       print("Computer Wins")    


 


      