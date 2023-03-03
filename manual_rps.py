import random
import time

# defines variables
computer_choice = []
user_choice = []
winner = []
user_wins = 0
computer_wins = 0

def get_computer_choice(): # Function to get the computers choice by randomly selecting from list
    # Globals
    global computer_choice
    # List of choices for the computer
    game_options = ["Rock", "Paper", "Scissors"]
    # randomly selects choice from list and assigns it to variable
    computer_choice = random.choice(game_options)
    # returns the computers choice
    return computer_choice

def get_user_choice(): # Function to receive and check the users choice
    # Globals
    global user_choice

    # Asks the user to input a letter based on what choice they want to make and converts it to lowercase
    user_choice = input("\nPlease choose; Rock, Paper or Scissors by typing R, P or S, respectively: ").lower() 

    # Assigns users input to either rock paper or scissors
    # then prints the users choice, and returns the users choice
    if user_choice == "r":
        user_choice = "Rock"
        return user_choice

    elif user_choice == "p":
        user_choice = "Paper"
        return user_choice

    elif user_choice == "s":
        user_choice = "Scissors"
        return user_choice

    # asks the user to re-enter their input if it was not either "R", "P" or "S"
    else:
        print("\nPlease enter 'R' for Rock, 'P' for Paper or 'S' for Scissors")
        get_user_choice()
    
    print(user_choice)
    

def get_winner(computer_choice, user_choice): # Function to take the choices of the user and computer and return the result of the game
    # Globals
    global winner
    global user_wins
    global computer_wins

# prints the computers once the user has chosen

    print(f"\nYou chose {user_choice}\n")
    print(f"The computer chose {computer_choice}")

# If the result is a tie 
    if computer_choice == user_choice:
        print("\nIt is a tie!\n")
    else:
    # If statements to figure out who won
        # -- Rock & Paper 
        if computer_choice == "Rock" and user_choice == "Paper": winner = "User"
        elif user_choice == "Rock" and computer_choice == "Paper": winner = "Computer"
        # -- Paper & Scissors
        elif computer_choice == "Paper" and user_choice == "Scissors": winner = "User"
        elif user_choice == "Paper" and computer_choice == "Scissors": winner = "Computer"
        # -- Scissors & Rock 
        elif computer_choice == "Scissors" and user_choice == "Rock": winner = "User"
        elif user_choice == "Scissors" and computer_choice == "Rock": winner = "Computer"

    # Returns the winner 
        if winner == "User":
            print("\nYou win this round!\n")
            user_wins += 1
        elif winner == "Computer":
            print("\nThe Computer wins this round\n")
            computer_wins += 1
        # Prints current no. of wins by user and computer
        print(f"User wins: {user_wins}")
        print(f"Computer wins: {computer_wins}\n")
# End of get_winner()

def play(): # function to call all other functions and in doing so, play the game of rock, paper, scissors
    # While loop that runs the game until either the computer or user wins = 2
    while computer_wins != 2 and user_wins != 2:
        # Prints 
        if computer_wins + user_wins == 0:
            pass
        else:
            print("Best out of three to win the game!")

        # Calls functions to play the game 
        get_computer_choice()
        get_user_choice()
        get_winner(computer_choice, user_choice)

    # Checks whether anyone has won the game yet by accumulating 2 wins and, if so, ends the image capture
    else:
        if computer_wins == 2:
            print("You lost this game, the Computer wins!\n")
        elif user_wins == 2:
            print("You won the game!\n")
# End of play()

play()