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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

input_1 = input("You enter a dungeon. There are 2 paths. Do you want to go left or right?").lower()

if input_1 == "left":
    input_2 = input("You reach an area with a lake. You look behind you and there are a bunch of skeletons approaching you. Do you want to fight or swim?").lower()
    if input_2 == "swim":
        print("A trout lives in the lake and eats you. Game Over!")
    else:
        door = input("You manage to fend them off. You encounter three doors. Red, Yellow and Blue are the colors of the doors. Which one do you want to go inside?").lower()
        if door == "yellow":
            print("You Win!")
        elif door == "red":
            print("Floor is Java. You get bored to death.")
        elif door == "blue":
            print("You get devoured by man-eating insects. Game over!")
        else:
            print("That's not a valid door color?. You get pulled into abyss(Out of bounds exception!)")
else:
    print("You fell in a hole. Game Over!")



