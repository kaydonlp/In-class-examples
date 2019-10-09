#Lock Program
#KaydonPayne\
#9/23/19

userNames = "Kaydon"
password = "Passcode"

user= input("Enter your username")
user_pass= input("Enter your Password")

if user == userNames:
    if user_pass == password:
        print("You're in" +user)
    else:
        print("Wrong Password")
elif user != userNames:
    print("Not a good username")
else:
    print("I don't know how you got here")


input()
