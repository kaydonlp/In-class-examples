#Kaydon Payne
#Programming Python 1&2
# 9/11/19

#10+ Variables
time = input ("Time:")
place = input("place/house:")
name = input("Name: " )
adjOne = input("Adjective:")
verbOne = input("Verb:")
animal = input("animal")
PluralNoun = input(" Plural Noun:")
nounOne = input("Noun:")
verbEd = input("Verb ending with -ing")
person2 = input("Name:")
adjThree = input ("Adjective")
nounThree = input ("Noun:")
action = input ("Action taking place:")

print( str.format("""Once upon a {} there was a man named {}, he lived in a {}. One day while he was {} he saw a {}{}.
As he kept {} he saw more {}. As he looked closer he noticed they were {}. When the {} saw the {}s they began to {}.
This made the man want to go home. But then he met {}. {} was {} and when they started talking they found out they had a lot on in common, but right as this happened they saw the
{}{}coming to fight them. So they ran away back to his {}."
""",time,name,place,verbOne,adjOne,animal,verbOne,PluralNoun,verbEd,animal,PluralNoun,action, person2,adjThree,person2,adjThree,action,PluralNoun,place))  

input()
