import random
import computerVision.model_copy as model_copy


class rockpaperscissors:
    # defines variables to the possible game choices and assigns releavent string to each one
    def __init__(self):
        self.rock = "Rock"
        self.paper = "Paper"
        self.scissors = "Scissors"
        self.nothing = "Nothing"
        # defines variabels
        self.computer_choice = []
        self.user_choice = []
        self.winner = []


    def get_computer_choice(self): # Function to get the computers choice by randomly selecting from list
        # list containing possible choices
        game_options = ["Rock", "Paper", "Scissors"]
        # randomly selects choice from list and assigns it to variable
        self.computer_choice = random.choice(game_options)
        # returns the computers choice
        return self.computer_choice


    def get_user_choice(self): 
        self.user_choice = model_copy.get_prediction()
        print(self.user_choice)

        if self.user_choice == "Rock":
            self.user_choice = self.rock
            print(f"\nYou chose: {self.user_choice}\n")
            return self.user_choice

        elif self.user_choice == "Paper":
            self.user_choice = self.paper
            print(f"\nYou chose: {self.user_choice}\n")
            return self.user_choice

        elif self.user_choice == "Scissors":
            self.user_choice = self.scissors
            print(f"\nYou chose: {self.user_choice}\n")
            return self.user_choice

        elif self.user_choice == "Nothing":
            self.user_choice = self.nothing
            print(f"\nYou chose: {self.nothing}, please try again!\n")
            return self.user_choice


    def get_winner(self, computer_choice, user_choice): # Function to take the choices of the user and computer and return the result of the game

    # prints the computers once the user has chosen
        print(f"The Computer chose {self.computer_choice}")

    # If the result is a tie 
        if self.computer_choice == self.user_choice:
            print("\nIt is a tie!\n")
        else:
        # Code to figure out who won
            # -- Rock & Paper 
            if self.computer_choice == self.rock and self.user_choice == self.paper:
                self.winner = "User"
            elif self.user_choice == self.rock and self.computer_choice == self.paper:
                self.winner = "Computer"
            # -- Paper & Scissors
            elif self.computer_choice == self.paper and self.user_choice == self.scissors:
                self.winner = "User"
            elif self.user_choice == self.paper and self.computer_choice == self.scissors:
                self.winner = "Computer"
            # -- Scissors & Rock 
            elif self.computer_choice == self.scissors and self.user_choice == self.rock:
                self.winner = "User"
            elif self.user_choice == self.scissors and self.computer_choice == self.rock:
                self.winner = "Computer"
        # Returns the winner 
            if self.winner == "User":
                return print("\nYou win!\n")
            elif self.winner == "Computer":
                return print("\nYou lose\n")


    def play(self): # function to call all other functions and in doing so, play the game of rock, paper, scissors
        rps.get_computer_choice()
        rps.get_user_choice()
        rps.get_winner(rps.computer_choice, rps.user_choice)
        

rps = rockpaperscissors()
rps.play()