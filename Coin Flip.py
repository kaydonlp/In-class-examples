#Kaydon Payne
#9/25/19
#Programming Python





import random
def coinflip(x):
    if x.isdigit():
        x=int(x)
        if x>0:
            for i in range(x):
                flip = random.randint(1,2)
            if num == 1:
                print("""
        _.-'~~`~~'-._
     .'`  B   E   R  `'.
    / I               T \\
  /`       .-'~"-.       `\\
 ; L      / `-    \      Y ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \ |        |
;        `~~;     \\        ;
 ;  INGODWE /      \\)P    ;
  \\  TRUST '.___.-'`"     /
   `\\                   /`
     '._   1 9 9 7   _.'
        `'-..,,,..-'`""")
            else:
                print("Tails ")
    else:
            print ("How did you get here??")
            
num = input("How many coins do you want to flip")
coinflip(num)
