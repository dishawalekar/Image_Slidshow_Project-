def quiz_game():
    score = 0
    print("Welcome to the Quize Game\n")
    
    #question 1
print("Q1. What is the Capital of India ?")
print("A.MUmbai")
print("B.Pune")
print("C.Delhi")
print("D.Kanpur") 
ans=input("Enter yours Answer(A/B/C/D):").upper() 
if ans == "C" :
    print("Correct\n")
    score += 1   # type: ignore
else:
    print(" Wrong!Correct is C\n")

#question 2
print("Q2.Which langauge is used to web development ?")
print("A.CSS")
print("B.HTML")
print("C.Python")
print("D.CPP") 
ans=input("Enter yours Answer(A/B/C/D):").upper() 
if ans == "B" :
    print("Correct\n")
    score += 1 
else:
    print(" Wrong!Correct is B\n") 

    #Question 3 
    print("Q3.Scope resolution Operator is dnoted by ?")
    print("A.<")
    print("B.+")
    print("C.::")
    print("D.=") 
    ans=input("Enter the your Answer(A/B/C/D):").upper()
    if ans == "C":
        print("Correct\n")
        score += 1 
    else:
        print("Wrong! Correct Answer is C\n") 

        #Question 4
    print("Q4.Which device is use to input data ? \n")
    print("A. Mouse")
    print("B.Printer")
    print("C.Speaker")
    print("D.Keyboard") 
    ans=input("Enter the your Answer(A/B/C/D):").upper()
    if ans == "D":
        print("Correct\n")
        score += 1 
    else:
        print("Wrong! Correct Answer is D\n") 

        #Question 5
        print("Whta is  18 *2 ?")
        print("A. 36")
        print("B.70")
        print("C.32")
        print("D.98") 
        ans=input("Enter the your Answer(A/B/C/D):").upper()
    if ans == "A":
        print("Correct\n")
        score += 1 
    else:
        print("Wrong! Correct Answer is A\n") 

        print("Quize is Finished1")
        print("Your Score:", score," /5 ") 
        quiz_game()




