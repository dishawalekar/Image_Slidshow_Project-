student={}

while True:
    print("\n--------STUDENT MANAGER APP------")
    print("1.Add Student")
    print("2.View Student")
    print("3.Check Result")
    print("4.Exit") 

    choice=input("Enter your choice:")

    #add student
    if choice == "1":
        name=input("Enter student name:")
        marks=int(input("Enter marks:"))
        student[name]=marks
        print(f"{name} Successfulyy Added!")

    #View student
    elif choice == "2":
        if  not student:
            print("not student found!")
        else:
            for name,marks in student.items():
                print(name,":" ,marks)    

   # check result
    elif choice == "3":
        name=input("Enter Student name:") 
        if name in student:
            marks = student[name]
        
            if marks >=35:
                print("Pass") 
            else:
                print("Fail")             
        else:
            print("Student not found!")

    # Exit 
    elif choice == "4":
        print("Exiting....")
        break
    else:
        print("Invalid input")


