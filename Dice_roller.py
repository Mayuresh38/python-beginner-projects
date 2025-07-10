#Loop
#Ask: roll the dice?
#If user say y
#   Generate tow random number
#If user enters n
#   print thank you message
#   Terminate
#Else
#    print Invalid choice


import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"({dice1}, {dice2})")

    elif choice == "n":
        print("Thanks for playing")
        break
    else:
        print("Invalid choice!")




    
