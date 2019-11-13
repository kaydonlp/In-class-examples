#Binary Guess
#10/30/19
#Kaydon Payne
import random

def guessbot():
    mr = 1
    mar = 10000
    rnum = int(input("What number would you like to have 1 through 10,000"))

    trys = 0

    gnum = random.randint(mr,mar)
    trys +=1
    print(gnum)
    print(rnum)

    while gnum != rnum:

        print("Checking")
        if gnum > rnum:
            print("Guess Lower")
            mar = gnum
        else:
            print("Guess Higher")
            mr = gnum+1
        print("Getting New Guess")
        gnum = random.randint(mr,mar)
        trys +=1
        print("Trys: ", trys)


    print("Your number was: ",rnum)
    print("It took",trys,"tries to guess your number")
