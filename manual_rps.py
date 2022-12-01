import random

def get_computer_choice(): # Function to get the computers choice by randomly selecting from list
    # list containing possible choices
    game_choices = ["Rock", "Paper", "Scissors"]
    # randomly selects choice from list and assigns it to variable
    computer_choice = random.choice(game_choices)
    # prints the computers choice
    print(computer_choice)

def get_user_choice(): # Function to receive and check the users choice
    # Asks the user to input a letter based on what choice they want to make and converts it to lowercase
    user_choice = input("\n Please choose; Rock, Paper or Scissors by typing R, P or S, respectively").lower() 

# Assigns users input to either rock paper or scissors
# and prints the users choice
    if user_choice == 'r':
        print('You chose Rock.')
    elif user_choice == 'p':
        print('You chose Paper.')
    elif user_choice == 's':
        print('You chose Scissors.')

# asks the user to re-enter their input if it was not either 'R', 'P' or 'S'
    else:
        print("Please enter 'R' for Rock, 'P' for Paper or 'S' for Scissors")
        get_user_choice()


get_computer_choice()
get_user_choice()
