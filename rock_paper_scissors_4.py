#APPLY THE DRY PRINCIPLE

import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = {ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, or, SCissors? (R/P/S): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")

def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == PAPER and computer_choice == ROCK) or 
        (user_choice == SCISSORS and computer_choice == PAPER)):
        print("You win")
    else:
        print("You lose")

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input('Continue? (Y/N): ').lower()
        if should_continue == 'n':
            break
        elif should_continue == 'y':
            continue
        else:
            print("Invalid Choice!")
            

play_game()


