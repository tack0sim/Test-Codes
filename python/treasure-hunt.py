print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice_1 = input("Do you want Right or left\n")
choice_1 = choice_1.lower()
if choice_1 == "left":
    choice_2 = input("Do you to swim or wait?\n")
    choice_2 = choice_2.lower()
    if choice_2 == "wait":
        choice_3 = input("Which door?Red , Blue , Yellow\n")
        choice_3 = choice_3.lower()
        if choice_3 == "red":
            print("Burnt in Fire")
        elif choice_3 == "yellow":
            print("You Win")
        elif choice_3 == "blue":
            print("Eaten by beasts")
        else :
            print("Game Over")
    elif choice_2 == "Swim":
        print("Attacked by trout")
    else :
        print("Game Over")
elif choice_1 == "Right":
    print("Fall into a hole")
else :
    print("Game Over")