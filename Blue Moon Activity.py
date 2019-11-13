#Kaydon Payne
#10/3/19
#Blue Moon Activity




#Get Inputs from User

moon = input("Is there a blue moon tonight(Yes /No)")
weekday = input("What is the day of the week(Monday-Sunday)")
dayofmonth = input("What is the day of the month(1-31)")

dayofmonth = str(dayofmonth)
weekday2 = weekday.title()
    #If theres a blue moon play "Once in a Blue Moon"

if moon == ("yes") or moon == ("Yes"):
    print("Play Song: Once in a Blue Moon")


#Weekday Songs
elif dayofmonth <= str(7):
    if weekday2 == ("Monday"):
        print("Play Song: Manic Monday")

    elif weekday2 == ("Tuesday"):
        print("Play Song: Tuesday's Gone")

    elif weekday2 == ("Wednesday"):
        print("Play Song: Just Wednesday")

    elif weekday2 == ("Thursday"):
        print("Play Song: Sweet Thursday")

    elif weekday2 == ("Friday"):
        print("Play Song: Friday I'm in Love")

    elif weekday2 == ("Saturday"):
        print("Play Song: Saturday in the Park")

    elif weekday2 == ("Sunday"):
        print("Play Song: Lazing on a Sunday Afternoon")
    else:
        print("Play Song: Days of the Week")


elif dayofmonth >str(7) :
    print("Play Song: Day Dream Believer")





