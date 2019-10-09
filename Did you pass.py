#Did you pass
#Kaydon Payne
#9/23/19

myGrade = int(input("What is your grade number"))
myLetterGrade = "Not Assigned"
if  myGrade>=90:                                                  # myGrade is equal to or grater than 90
    myLetterGrade = "A"
elif myGrade>=80:                                             # myGrade is equal to or greater than 80
    myLetterGrade = "B"
elif myGrade >=70:
    myLetterGrade= "C"
elif myGrade>=60:
    myLetterGrade="D"
elif mygrade >=50:
    myGrade= "F"
else:
    print("Did you even try???")
                                              
print("My grade is:", myLetterGrade)
