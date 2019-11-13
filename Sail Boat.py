#Kaydon Payne
#SailBoat
#10-01-19

#Get Artists Name
artist = input("artists name:")
#Re-format to string
painting=str.format("""
+--------------------+
|        |>          |
|        |\\          |
|        | \\         |
|        |  \\        |
|        |   \\       |
|        |    \\      |
|  \==============/  |
|   \____________/   |
|                    |
|   {0:10.10}       |
+--------------------+""",artist)
#print the painting
print(painting)
#make runable from desktop  
input()

