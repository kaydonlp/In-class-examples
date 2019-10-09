def intro(name):
    print("""

    Welcome to """+name+"""
    please choose an option
    from the list below

    1: Option 1
    2: Option 2
    3. Option 3
    4: Quit""")

def Option1():
    print("Option 1")

#Example Menu
#Kaydon Payne
#9/25/19
#Programming Python 1 and 2

def Option2():
    print("Option 2")

def Option3():
    print("Options 3")
def option4():
    varify = input("Are you sure you want to quit")
    varify = varify.lower()
    if varify.contains("y"):
        return True
    else:
        return False



def menu():
    while True:
        intro("calculator")
        choice = input("pick an option 1, 2, 3, 4")
        if choice =="1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            varify = option4()
            if varify:
                break
            else:
                continue
        else:
            print("Thats not an options")

menu()
input("press enter to exit")



