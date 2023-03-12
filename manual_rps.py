import random
import time

class rockpaperscissors:
    # defines variables to the possible game choices and assigns releavent string to each one
    def __init__(self):
        self.rock = "Rock"
        self.paper = "Paper"
        self.scissors = "Scissors"
        self.nothing = "Nothing"
        # defines variables
        self.computer_choice = []
        self.user_choice = []
        self.winner = []
        self.user_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self): # Function to get the computers choice by randomly selecting from list
        # list containing possible choices
        game_options = ["Rock", "Paper", "Scissors"]
        # randomly selects choice from list and assigns it to variable
        self.computer_choice = random.choice(game_options)
        # returns the computers choice
        return self.computer_choice

    def get_user_choice(self):
        
        # Function to receive and check the users choice
        # Asks the user to input a letter based on what choice they want to make and converts it to lowercase
        self.user_choice = input("\nPlease choose; Rock, Paper or Scissors by typing R, P or S, respectively: ").lower() 

        # Assigns users input to either rock paper or scissors
        # then prints the users choice, and returns the users choice
        if self.user_choice == "r":
            self.user_choice = self.rock
            print(f"\nYou chose: {self.user_choice}\n")
            return self.user_choice

        elif self.user_choice == "p":
            self.user_choice = self.paper
            print(f"\nYou chose: {self.user_choice}\n")
            return self.user_choice

        elif self.user_choice == "s":
            self.user_choice = self.scissors
            print(f"\nYou chose: {self.user_choice}\n")
            return self.user_choice

        # asks the user to re-enter their input if it was not either "R", "P" or "S"
        else:
            print("\nPlease enter 'R' for Rock, 'P' for Paper or 'S' for Scissors")
            self.get_user_choice()
        

    def get_winner(self, computer_choice, user_choice): # Function to take the choices of the user and computer and return the result of the game

    # prints the computers once the user has chosen
        print(f"The Computer chose {self.computer_choice}")

    # If the result is a tie 
        if self.computer_choice == self.user_choice:
            print("\nIt is a tie!\n")
        else:
        # If statements to figure out who won
            # -- Rock & Paper 
            if self.computer_choice == self.rock and self.user_choice == self.paper: self.winner = "User"
            elif self.user_choice == self.rock and self.computer_choice == self.paper: self.winner = "Computer"
            # -- Paper & Scissors
            elif self.computer_choice == self.paper and self.user_choice == self.scissors: self.winner = "User"
            elif self.user_choice == self.paper and self.computer_choice == self.scissors: self.winner = "Computer"
            # -- Scissors & Rock 
            elif self.computer_choice == self.scissors and self.user_choice == self.rock: self.winner = "User"
            elif self.user_choice == self.scissors and self.computer_choice == self.rock: self.winner = "Computer"

        # Returns the winner 
            if self.winner == "User":
                print("\nYou win this round!\n")
                self.user_wins += 1
            elif self.winner == "Computer":
                print("\nThe Computer wins this round\n")
                self.computer_wins += 1
            # Prints current no. of wins by user and computer
            print(f"User wins: {self.user_wins}")
            print(f"Computer wins: {self.computer_wins}\n")
    # End of get_winner()

    def play(self): # function to call all other functions and in doing so, play the game of rock, paper, scissors
        # While loop that runs the game until either the computer or user wins = 2
        while self.computer_wins != 2 and self.user_wins != 2:
            # Prints 
            if self.computer_wins + self.user_wins == 0:
                pass
            else:
                print("\nBest out of three to win the game!")

            # Calls functions to play the game 
            self.get_computer_choice()
            self.get_user_choice()
            self.get_winner(self.computer_choice, self.user_choice)

        # Checks whether anyone has won the game yet by accumulating 2 wins and, if so, ends the image capture
        else:
            if self.computer_wins == 2:
                print("You lost this game, the Computer wins!\n")
            elif self.user_wins == 2:
                print("You won the game!\n")
    # End of play()
rps = rockpaperscissors()
rps.play()