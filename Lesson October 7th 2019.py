#Kaydon Payne
#10/7/19
#PRogramming 1 &2

inventory = ["Short Sword",
                        "Chain-Mail Armor",
                        "Helm",
                        "Boots",
                        "Pants",
                        "Shield",
                        "Healing Potion",
                        "Dagger",
                        "Mana Potion"]

print(max(inventory))
print(min(inventory))



stuff= ["Crystaline Bow", "Electric Infused Staff","3 Kegs of Rum","Dragon-Scale Armor"]
for item in stuff:
    inventory.append(item)

print(inventory)



inventory.remove("Healing Potion")
print(inventory)

hand = inventory.pop(-1)
print(inventory)
print(hand)

inventory.sort()
print(inventory)


#none of the above work with tuples because you cannot change tuples only lists^^^^^^^
x = inventory.index("Pants")
print (x)
#this one works with tuples and lists^^^^^^^^^

