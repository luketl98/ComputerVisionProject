import random

class rockpaperscissors:
    # defines variables to the possible game choices and assigns releavent string to each one
    def __init__(self):
        self.rock = "Rock"
        self.paper = "Paper"
        self.scissors = "Scissors"
        # defines variabels
        self.computer_choice = []
        self.user_choice = []
        self.winner = [10]

    def get_computer_choice(self): # Function to get the computers choice by randomly selecting from list
        # list containing possible choices
        game_options = ["Rock", "Paper", "Scissors"]
        # randomly selects choice from list and assigns it to variable
        self.computer_choice = random.choice(game_options)
        # prints the computers choice
        print(f"\ngetcompchoice: {self.computer_choice}")
        # returns the computers choice
        return self.computer_choice

    def get_user_choice(self): # Function to receive and check the users choice
        # Asks the user to input a letter based on what choice they want to make and converts it to lowercase
        self.user_choice = input("\nPlease choose; Rock, Paper or Scissors by typing R, P or S, respectively: ").lower() 
        # Assigns users input to either rock paper or scissors
        # and prints the users choice, and returns the users choice

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
            x.get_user_choice()
        

    def get_winner(self, computer_choice, user_choice): # Function to take the choices of the user and computer and return the result of the game

        print(x.get_computer_choice())
        print(x.get_user_choice(), 10)

    # Tie 
        if self.computer_choice == self.user_choice:
            print("Its a tie!")
        

    # Figure out who won
        # -- Rock & Paper 
        elif self.computer_choice == self.rock and self.user_choice == self.paper:
            self.winner = "User"
            return self.winner
        elif self.user_choice == self.rock and self.computer_choice == self.paper:
            self.winner = "Computer"
            return self.winner
        # -- Paper & Scissors
        elif self.computer_choice == self.paper and self.user_choice == self.scissors:
            self.winner = "User"
            return self.winner
        elif self.user_choice == self.paper and self.computer_choice == self.scissors:
            self.winner = "Computer"
            return self.winner
        # -- Scissors & Rock 
        elif self.computer_choice == self.scissors and self.user_choice == self.rock:
            self.winner = "User"
            return self.winner
        elif self.user_choice == self.scissors and self.computer_choice == self.rock:
            self.winner = "Computer"
            return self.winner

        return self.winner

        
    """ ----- What was wrong with this ? -----
    # user wins -- 
        if result == rock + paper:
            if computer_choice.count(paper) == 1:
                winner = "Computer"
                print("computer wins")
            elif user_choice.count(paper) == 1:
                winner = "User"
                print("user wins")
            return print(winner)

    #  -- comp wins
        if result == scissors + paper:
            if computer_choice.count(scissors) == 1:
                winner = "Computer"
                print("computer wins")
            elif user_choice.count(scissors) == 1:
                winner = "User"
                print("user wins")
            return print(winner)
        
    # -- 
        if result == rock + scissors:
            if computer_choice.count(rock) == 1:
                winner = "Computer"
                print("computer wins")
            elif user_choice.count(rock) == 1:
                winner = "User"
                print("user wins")
            return print(winner)

        pass
    """

x = rockpaperscissors()
x.get_winner(x.computer_choice, x.user_choice)