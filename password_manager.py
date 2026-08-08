import random
import string

password={}

#load exting password file
try:
    with open(password.txt,'r') as file:
     for line in file:
        website,pwd=line.strip().split(":")
        password[website]=pwd 
except:
      pass

def generate_password():
    chars=string.ascci_letters + string.digits + "!@#$%&"
    password = "".join(random.choice(chars) for _ in range(8))
    return password

while True:
    print("----PASSWORD GERERATOR----")
    print("1:Add password")
    print("2:View Password")
    print("3:Generate Password")
    print("4:Exit\n")

    choice = input("Enter your choice:")

    if choice == "1":
        site=input("Enter website:")
        pwd=input("Enter password:")

        password[site] = pwd 

        with open("password.txt","a") as file:
            file.write(f"{site} : {pwd}\n")

        print("Sucessfully Save!") 
         
    elif choice == "2":
        if not  password:
            print("No data")
        else:
            for site,pwd in password.items():
                print(site,":",pwd)

    elif choice == "3":
        print("Generate Password",generate_password())

    elif choice == "4":
        print("Ok byeee")
        break
    else:
        print("Invalide input")

