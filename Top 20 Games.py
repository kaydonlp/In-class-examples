



import random

top_games = ["Rocket League",
" Player Unknown BattleGrounds",
"Smash Bros Brawl",
"BlackJack",
"CounterStrike",
"UnderTale",
"5 card draw",
"ShellShock Live",
"Oxygen Not Included",
"Teamfight Tactics",
"Mario Monopoly", 
"Life",
"Detroit: Become Human",
"BeamNG Drive",
"Black Ops 4",
"Kindergarten",
"Kindergarten 2",
"Subnautica",
"Worbital",
"Slime Rancher"]

print(type(top_games))

print(len(top_games))

##print(top_games)
#print(top_games[12:20])

#for i in top_games:
  #  print(i)
for i in range(0,len(top_games)):
    print("-------------",top_games[i])

num = random.randint(0,len(top_games)-1)

print(top_games[num])
if len(top_games) < 20:
    print("Fail")
elif "fortnite"in top_games or "Fortnite" in top_games:
    print("Fail")

elif top_games[0] != "Rocket League":
    print("Fail")
else:
    print("pass")

for i in top_games:
    if i =="Rocket League":
        print("Found Favorite game")
    else:
        print("not it")

top_games[5] = "Updated"

print(top_games)
