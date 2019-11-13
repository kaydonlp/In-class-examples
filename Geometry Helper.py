#Taya Martinez, Kaydon Payne, Jessica Adams, Isaac Lehman
#9/11/19
#Geometry Homework Helper

#I added in ascii art since I may or may not be in class because of a funeral...-Kaydon Payne

while True:

  print("""
             _            _       _             
    ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
   / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
  | (_| (_| | | (__| |_| | | (_| | || (_) | |   
   \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

  """)
  print("What problem are you trying to solve?")
  print("Perimeter of a square = 1")
  print("Area of a square = 2")
  print("Circumference of a circle = 3")
  print("Area of a triangle = 4")
  print("Volume of a cube = 5")
  choice=input("Type the corresponding number: ")

  if choice=="1":
    #Perimeter of a square
    print("""
               _            _       _             
      ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
     / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | (_| (_| | | (__| |_| | | (_| | || (_) | |   
     \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

    """)
    print("Finding Perimeter of a Square")
    side_length = input("What is the side length of the square?")
    perimeter = int(side_length)*4
    square1 = str.format("""
       _______
      |       |
      |       |
      |       |
      |_______|

    Side Length: {}
    Perimeter: {}
    """,side_length,perimeter)
    print(square1)
    input()
  elif choice=="2":
    #Area of a square

    print("""
               _            _       _             
      ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
     / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | (_| (_| | | (__| |_| | | (_| | || (_) | |   
     \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

    """)
    print("Finding The Area of a Square")
    side_length = input("What is the side length of the square?")
    area = int(side_length)*int(side_length)
    square = str.format("""
     _______
    |       |
    |       |
    |       |
    |_______|

    Side Length: {}
    Area:{} 
    """,side_length,area)
    print(square)
    input()

  elif choice=="3":
    #Circumference of a circle
    print("""
               _            _       _             
      ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
     / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | (_| (_| | | (__| |_| | | (_| | || (_) | |   
     \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

    """)
    pi=3.14159265
    print("""Circumference of a circle = 2πR""")
    rad=input("Radius: ")
    cir=float(2)*float(pi)*float(rad)
    cir_Final=str.format("{0:.2f}",cir)

    circle = str.format(""" 
                 _____
              .-'     '-.
            .'           '.
           /               \\
          ;                 ;
          |                 |
          ;                 ;
           \\               /
            '.           .'
              '-._____.-'


    Radius: {}
    Circumference: {}
    """,rad,cir_Final)
    print(circle)
    input()
  elif choice=="4":
    #-AREA OF TRIANGLE-
    #variables for base and height--(triHeight is height, triBase is base)
    print("""
               _            _       _             
      ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
     / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | (_| (_| | | (__| |_| | | (_| | || (_) | |   
     \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

    """)
    print("finding the Area of Triangles")
    triHeight=input("enter triangle's height: ")
    triBase=input("enter triangle's base length: ")
      #triArea is area of triangle--(base*height/2)
    triArea= float(triHeight)*float(triBase)/2
      #printing solution
    triangle = str.format("""
              _____
             /    /\\
            /    /  \\
           /    /    \\
          /    /  /\\  \\
         /    /  /  \\  \\
        /    /  /\\   \\  \\
       /    /  /  \\   \\  \\
      /    /__/____\\   \\  \\
     /              \\   \\  \\
    /________________\\   \\  \\
    \_____________________\\ /


    Base: {}
    Height: {}
    Area: {}
    """,triHeight,triBase,triArea)
    print(triangle)
    input()



  elif choice=="5":
    #Volume Of A Cube
    print("""
               _            _       _             
      ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
     / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | (_| (_| | | (__| |_| | | (_| | || (_) | |   
     \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

    """)
    print("Volume of a Cube")
    a = input ("what is the length of any one side: ")
    volume = int(a)*int(a)*int(a)
    cube = str.format("""



    @ + + + + + + + + + + + @
    +\\                      +\\
    + \\                     + \\
    +  \\                    +  \\
    +   \\                   +   \\
    +    @ + + + + + + + + +++ + @
    +    +                  +    +
    +    +                  +    +
    +    +                  +    +
    +    +                  +    +
    +    +                  +    +
    +    +                  +    +
    @ + +++ + + + + + + + + @    +
     \\   +                   \\   +
      \\  +                    \\  +
       \\ +                     \\ +
        \\+                      \\+
         @ + + + + + + + + + + + @


    Length: {0}
    Width: {0}
    Height: {0}
    Volume: {1}
    """,a,volume)

    print(cube)
    input()

    #It's perfect! Great job team! You all slayed it with this project, we got it done, and it looks suteki!
