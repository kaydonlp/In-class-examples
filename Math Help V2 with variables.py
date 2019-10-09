#Taya Martinez, Kaydon Payne, Jessica Adams, Isaac Lehman
#Testers: Bales, Greyson, Ian Christensen, Jayden Williams,Max Virkus
#9/11/19
#Geometry Homework Helper


#Perm of sqr
## If you put letters it exits program

#Area of sqr
## Letters break it
## special charecters break

#Circumference of a circle
## Letters break//
## Special charecters break

#area of a triangle
## Letters break

#Volume of a cube
## letters exit program




#I added in ascii art since I may or may not be in class because of a funeral...-Kaydon Payne


def calcP():
    print("""
               _            _       _             
      ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
     / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | (_| (_| | | (__| |_| | | (_| | || (_) | |   
     \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

    """)


def menu():
  while True:
    calcP()
    print ("""What problem are you trying to solve?")
      Perimeter of a square = 1")
      Area of a square = 2")
      Circumference of a circle = 3")
      Area of a triangle = 4")
      Volume of a cube = 5")
      To leave type 'end'""")
    choice=input("Type the corresponding number: ")
    if choice=="1":
      squareperm()
    elif choice=="2":
      squarearea()
    elif choice=="3":
      circlecircum()
    elif choice=="4":
      areatriangle()
    elif choice=="5":
      cubevolume()

def squareperm():
    print("Finding Perimeter of a Square")
    side_length = input("What is the side length of the square?")
    if side_length.isdigit:
      perimeter = int(side_length)*4
      perimeter = str(perimeter)+"ft"
      square1 = str.format("""  
           _______
          |       |
          |       |{0}ft
          | {1:^6.2e}|
          |_______|

      Side Length: {0}ft
      Perimeter: {1}
      """,side_length,perimeter)
      print(square1)
      input()
    else:
      print("A number!")
      squareperm()

def squarearea():
    print("Finding The Area of a Square")
    side_length = input("What is the side length of the square?")
    area = int(side_length)*int(side_length)
    area = str(area)+"ft^2"
    square = str.format("""
      
       _______
      |       |
      |       |{0}ft
      | {1:^5.2e}|
      |_______|
          

    Side Length: {0}ft
    Area:{1}
    """,side_length,area)
    print(square)
    input()

def circlecircum():
    pi=3.14159265
    print("""Circumference of a circle = 2πR""")
    rad=input("Radius: ")
    cir=float(2)*float(pi)*float(rad)
    cir_Final=str.format("{0:.2f}",cir)
    cir_Final=cir_Final+"ft"
    circle = str.format("""
                     
                 _____
              .-'     '-.
            .'           '.
           /               \\
          ;    {0:^5.2e}        ;
          |---------        |{1}ft
          ;                 ;
           \\               /
            '.           .'
              '-._____.-'
                  

    Radius: {1}ft
    Circumference: {0}ft
    """,rad,cir_Final)
    print(circle)
    input()


def cubevolume():
    print("Volume of a Cube")
    a = input ("what is the length of any one side: ")
    volume = float(a)*float(a)*float(a)
    cube = str.format("""



    @ + + + + + + + + + + + @
    +\\                      +\\
    + \\                     + \\
    +  \\                    +  \\{0}ft
    +   \\                   +   \\
    +    @ + + + + + + + + +++ + @
    +    +                  +    +
    +    +                  +    +
    +    +                  +    +
    +    +     {1:^3.2e}     +    + {0}ft
    +    +                  +    +
    +    +                  +    +
    @ + +++ + + + + + + + + @    +
     \\   +                   \\   +
      \\  +                    \\  +
       \\ +                     \\ +
        \\+                      \\+
         @ + + + + + + + + + + + @
                      {0}ft

    Length: {0}ft
    Width: {0}ft
    Height: {0}ft
    Volume: {1}ft^3
    """,a,volume)

    print(cube)
    input()


    
def areatriangle():
    triHeight=float(input("enter triangle's height: "))
    triBase=float(input("enter triangle's base: "))

    triArea= float(triHeight)*float(triBase)/2


    print(str.format("""\


                |        | 
               /|\\       | 
              / | \\      | 
             /  |  \\   {0:.2.2e}
            /   |   \\    | 
           /    |    \\   | 
          ------|------  |
             {1:.2.2e} 
        Area= {2:.2.2e}" un. squared """,triHeight,triBase,triArea))


    input()





    
def areasquare():
  
    print("Finding The Area of a Square")
    side_length = input("What is the side length of the square?")
    area = int(side_length)*int(side_length)
    area = str(area)+"ft^2"
    square = str.format("""
      
       _______
      |       |
      |       |{0}ft
      | {1:^5.2e}|
      |_______|
          

    Side Length: {0}ft
    Area:{1}
    """,side_length,area)
    print(square)
    input()




menu()
