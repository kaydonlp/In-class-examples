#Kaydon Payne
#10/28/19
#Programming Python 1 & 2
#Guess My Number Program
import random
#get a number and make sure it is within the range and returns the number
def numInRange(rmin,rmax,maxguess):
    while True:
        guess = input("Choose a Number between " +str(rmin)+ "and " +str(rmax) +"\n")
        if guess.isdigit():
            guess = int(guess)
            if guess >= rmin and guess <= rmax:
                return guess
            else:
                print ("Not a Good Value " )
def Number_Game(rmin,rmax,maxguess):
    num = random.randint(rmin,rmax)
    guess = numInRange(rmin, rmax,maxguess)
    guessNum = 0
    guessNum+=1
    while guess != num and guessNum != maxguess:
        if guess >=num:
            print("Guess Lower")
        else:
            print("Guess Higher")
        guess = numInRange(rmin, rmax,maxguess)
        guessNum+=1
    if guess == num:
        print("""You Guessed the number, Congratulations! """)
        print("""

 ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,                                                                              .
,                  I                                     II                    .
,  .,,,,,,,,,,,,,+II,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,+?++,,,,,,,,,,,,,,,,,,,
,  ,            ++++      7777$$$$???+++=~~,....,=$877   +++?$                 ,
,  ,           77+++      7I77$$$$????++=~~,....,=$877    III$    I            ,
,  ,       I   777+$ZZZ7  ZI777$$$????++=~~,,...,=$$77  ??7I?:O  II            ,
,  ,       I?   7+$Z   ZZZZI777$$$????++=~~,,...,=$$77?7I    $:  +I            ,
,  ,      +I+    =Z        I777$$$I???++=~~:,...~I$$77 III+??I?Z++++           ,
,  ,      ++++ 777Z+I?I    7777$$$I???++=~~:,..,~I$777  I+++?7OOI+I$           ,
,  ,      $$+7 77+Z++?     ZI77$$$I???++=~~:,,,,=I$77    +++?IZOI7$$           ,
,  ,      $$77777=8+       ZI777$$I???++=~~:,,,,=I$77        I=$ 7$    77      ,
,  , 77    $$777777Z77     ZI777$$I???++=~~:,,,~=$$77    III+O: OZ   +7+       ,
,  ,  77??   7 7++787       I777ZZ7???++=~:~:::~I$777     I+O:$7 O $O+++       ,
,  ,  ????$  777+===8       ZI77ZO$I??++=~~~:::=I$777      +?O777O $I++        ,
,  ,   ??I7$  7777+7=8      ZI77$O$I??+++=~~~~~=$$77       ?O 777 O$$$         ,
,  ,     $$$ 777 II  78      I77$O$I???++=~~~~~I$$77      ??II+ +O$I           ,
,  ,        $.? +I++  7Z     ZI77OO7I??++==~~~=$O77     O:? ++++ OO            ,
,  ,       Z 7 I+++    77     I77OO$I???++=~~~IOO7O    Z?  7+++$$   $???7$$    ,
,  ,$$7+III  777?++ $    7Z   ZI7Z8$II???+====$8Z7   O~?  77 II$$7Z$777777     ,
,  , 77I?II$$  777 $$I     7$  I778O$II??++=+I887O O??    ????$$$$$$7777       ,
,  ,  IIIII$$$777 ????  7    7$ZI7O8$II??++++O8O7O??   $  ???I+7$$$$$          ,
,  ,      $$$$$77 I???  77     7I7$8Z$II????I887O?    $$  III$  7$             ,
,  ,         777 ZZII$ +7++    7 I7O8$$IIII$887O ?   II$I $Z7Z 7 Z$II?7        ,
,  ,       I77O 7 ZZ$$ I==?       778O$$$$$88OO    7 IIII  ZZZ OZ$$I?7$$Z      ,
,  ,  ZZ$$??I7ZZZ7ZZZ  ++=?$       OO88OOOD8OO    77 III7O ZZ 7ZZ$77777$       ,
,  ,   ZZ$II777ZZZ7ZZ  7777 77?     OOOOOO8O    ???7  Z7O$$ Z ZZZZZ77          ,
,  ,     $7777ZZZZ7Z  77777 77??     =O$7Z=     ????  OOO.$7                   ,
,  ,              7  7  ZII ????I    ?88887     7???+ OO.7 OOOOO               ,
,  ,            77OOOOO7$Z +7III$$   ??87O     ZZZZ 7? 7 OOOIO$$II             ,
,  ,          7IIII7ZZZZ  $7  $$Z$   ??87O$    ZZZ  7$Z$  OOO$III$$D           ,
,  ,        ZZZ7III7ZZ   7OOO 77ZZ$  ?IZ7OI    Z77$$$$$$?     III7$$           ,
,  ,          77I7      I7OOOZOZ  777~Z777+  7    777???+++                    ,
,  ,                   IIII7ZZZ      ~8777++       77?++++II                   ,
,  ,                 ZZ$III7Z       ~?Z7777+           ?++?I                   ,
,  ,                 Z77II        7??777777777                                 ,
,  ,                            7???????????===?                               ,
,  ,                          D87?7OOOZ777ZOO7=?ZZ                             ,
,  ,                         888888888888888888ZZZZ                            ,
,  ,                         88DDDDDDDDDD888OOOZZZZ                            ,
,  ,                         88DDDDDDDDDD888OOOZZZ8                            ,
,  ,                             NDDDDDDDDDDDDD                                ,
,  ,                                                                           ,
,..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, 
""")
    else:
        print("You Lost, Better Luck next time! ")

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


def Custom_Setting():
    rmin = input("What Minimum would you Like to have?")
    rmax = input("What Maximum would you Like to have?")
    maxguess = input("What Number of Guesses would you like to have?")
    rmin = int(rmin)
    rmax = int(rmax)
    maxguess = int(maxguess)
    Number_Game(rmin,rmax,maxguess)

    
def options_Menu():
    print("""
    Options
----------------
Press 1 for Easy
Press 2 for Medium
Press 3 for Hard
Press 4 for Custom
""")
    choice = input("Choice: ")
    if choice.isdigit:
        choice = int(choice)
        if choice >= 1 and choice  <= 4:
            if choice ==  1:
                rmin = 1
                rmax = 10
                maxguess = 5
                Number_Game(rmin,rmax,maxguess)
            if choice == 2:
                rmin = 1
                rmax = 20
                maxguess = 3
                Number_Game(rmin,rmax,maxguess)
            if choice == 3:
              rmin = 1
              rmax = 30
              maxguess = 2
              Number_Game(rmin,rmax,maxguess)
            if choice ==4:
                Custom_Setting()

def Game_Menu():
        print("""
            Menu
    -------------------
Options Menu press 1
Play Game Press 2
Play with Bot Press 3
Quit Game Press 4
    """)
        option = input("Choice: ")
        if option.isdigit:
            option = int(option)
            if option >=1 and option <=3:
                if option ==  1:
                    options_Menu()
                if option == 2:
                    rmin = 1
                    rmax = 10
                    maxguess = 5
                    Number_Game(rmin,rmax,maxguess)
                if option == 3:
                    guessbot()
                if option == 4:
                    quit()
Game_Menu()
input()
