# Aak the user to amke a choice
# If choice is not valid
#    print an error
# let the computer to make a choice
# Print choices (emojis)
# Determine the Winner
# Ask the user if they want to continue
# If not
#  Terminate

import random

emojis = {'r': '🪨', 's': '✂️', 'p': '📃'}
choices = ('r', 'p', 's')

while True:
    user_choice = input("Rock, Paper, or, SCissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid Choice!")
        continue

    computer_choice = random.choice(choices)

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == 'r' and computer_choice == "s") or 
        (user_choice == 'p' and computer_choice == "r") or 
        (user_choice == 's' and computer_choice == "p")):
        print("You win")
    else:
        print("You lose")

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break
    elif should_continue == 'y':
        continue
    else:
        print("Invalid Choice!")

    


