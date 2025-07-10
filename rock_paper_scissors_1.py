import random

while True:
    
    computer_choice = random.choice(['r',' p', 's'])
    choice = input("Rock, Paper, or, SCissors? (r/p/s): ").lower()

    if choice == 'r':
        print("You chose Rock")
    elif choice == 'p':
        print("You chose Paper")
    elif choice == 's':
        print("You chose Scissors")
    else:
        print("Invalid choice")

    
    if computer_choice == 'r':
        print("computer chose Rock")
    elif computer_choice == 'p':
        print("computer chose Paper")
    else:
        print("computer chose Scissors")


    if choice == 'r' and computer_choice == "s":
        print("You Win")
    elif choice == 'p' and computer_choice == 'r':
        print("You Win")
    elif choice == 's' and computer_choice == 'p':
        print("You Win")
    elif choice == computer_choice:
        print("Game Tie!")
    else:
        print("You Lose")

    continue_choice = input("Continue? (y/n): ")
    if continue_choice == 'n':
        print("Thanks for playing")
        break
    elif continue_choice == 'y':
        continue
    else:
        print("Please enter valid answer!")


        
    
   




    
