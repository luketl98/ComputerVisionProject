import random

# defines variables and assigns releavent string to each one
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

def get_computer_choice(): # Function to get the computers choice by randomly selecting from list
    # list containing possible choices
    game_options = ["Rock", "Paper", "Scissors"]
    # randomly selects choice from list and assigns it to variable
    computer_choice = random.choice(game_options)
    # prints the computers choice
    print(f"\ngetcompchoice: {computer_choice}")
    return computer_choice

def get_user_choice(): # Function to receive and check the users choice
    # Asks the user to input a letter based on what choice they want to make and converts it to lowercase
    user_choice = input("\nPlease choose; Rock, Paper or Scissors by typing R, P or S, respectively: ").lower() 
    # Assigns users input to either rock paper or scissors
    # and prints the users choice, and returns the users choice

# -------------
    # defines variables and assigns releavent string to each one
    #rock = "Rock"
    #paper = "Paper"
    #scissors = "Scissors"
# -------------

    if user_choice == "r":
        user_choice = rock
        print(f"\nYou chose: {user_choice}\n")
        return user_choice

    elif user_choice == "p":
        user_choice = paper
        print(f"\nYou chose: {user_choice}\n")
        return user_choice

    elif user_choice == "s":
        user_choice = scissors
        print(f"\nYou chose: {user_choice}\n")
        return user_choice

    # asks the user to re-enter their input if it was not either "R", "P" or "S"
    else:
        print("\nPlease enter 'R' for Rock, 'P' for Paper or 'S' for Scissors")
        get_user_choice()
    

def get_winner(): # Function to take the choices of the user and computer and return the result of the game

    computer_choice = get_computer_choice()
    user_choice = get_user_choice()

    # Tie 
    if computer_choice == user_choice:
        print("its a tie")

    result = computer_choice + user_choice

    winner = 0

    if result == rock + paper:
        result = paper
        if computer_choice.count(paper) == 1:
            winner = "Computer"
            print("computer wins")
        elif user_choice.count(paper) == 1:
            winner = "User"
            print("user wins")
        return print(winner)

# 1/2 Works (comp wins -- )
    if result == scissors + paper:
        result = scissors
        if computer_choice.count(scissors) == 1:
            winner = "Computer"
            print("computer wins")
        elif user_choice.count(scissors) == 1:
            winner = "User"
            print("user wins")
        return print(winner)
    
    if result == rock + scissors:
        result = rock
        if computer_choice.count(rock) == 1:
            winner = "Computer"
            print("computer wins")
        elif user_choice.count(rock) == 1:
            winner = "User"
            print("user wins")
        return print(winner)

    pass


get_winner()