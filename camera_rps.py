import random
import time
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class RockPaperScissors:
    # defines variables to the possible game choices and assigns releavent string to each one -
    def __init__(self):
        self.computer_choice = []
        self.user_choice = []
        self.winner = []
        self.user_wins = 0
        self.computer_wins = 0


    def get_computer_choice(self): # Function to get the computers choice by randomly selecting from list
        game_options = ["Rock", "Paper", "Scissors"] # list containing possible choices
        self.computer_choice = random.choice(game_options) # randomly selects choice from list and assigns it to variable


    def get_prediction(self): # Function to start the image capture and classify results 
            while True:
                ret, frame = cap.read()
                resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                data[0] = normalized_image
                prediction = model.predict(data, verbose=0)
                # Point between start of program and start of image capture
                cv2.imshow('frame', frame)
                result = np.argmax(prediction) # Find the result using numpy
                break

            return result


    def get_user_choice(self): # Determines the users choice via image capture 
        # Calls get_prediction and starts image capture to determine users choice
        self.user_choice = self.get_prediction()

        while self.user_choice == 3:
            self.get_prediction()

        # assign numpy.argmax result to a class and print 
        if self.user_choice == 0:
            self.user_choice = "Rock"
        elif self.user_choice == 1:
            self.user_choice = "Paper"
        elif self.user_choice == 2:
            self.user_choice = "Scissors"

        print(f"You chose {self.user_choice}\n")


    def get_winner(self, computer_choice, user_choice): # Function to take the choices of the user and computer and return the result of the game

        print(f"The Computer chose {self.computer_choice}")
    # If the result is a tie 
        if self.computer_choice == self.user_choice:
            print("\nIt is a tie!\n")
            self.winner = []
        else:
        # If statements to figure out who won
            # -- Rock & Paper 
            if self.computer_choice == "Rock" and self.user_choice == "Paper": self.winner = "User"
            elif self.user_choice == "Rock" and self.computer_choice == "Paper": self.winner = "Computer"
            # -- Paper & Scissors
            elif self.computer_choice == "Paper" and self.user_choice == "Scissors": self.winner = "User"
            elif self.user_choice == "Paper" and self.computer_choice == "Scissors": self.winner = "Computer"
            # -- Scissors & Rock 
            elif self.computer_choice == "Scissors" and self.user_choice == "Rock": self.winner = "User"
            elif self.user_choice == "Scissors" and self.computer_choice == "Rock": self.winner = "Computer"
            # -- If user_choice is nothing
            elif self.user_choice == "Nothing":
                self.winner = []
            
    # Returns the winner 
        if self.winner == "User":
            print("\nYou win this round!\n")
            self.user_wins += 1
        elif self.winner == "Computer":
            print("\nThe Computer wins this round\n")
            self.computer_wins += 1
        else:
            pass
        # Prints current no. of wins by user and computer
        print(f"User wins: {self.user_wins}")
        print(f"Computer wins: {self.computer_wins}\n")


    def play(self):     # function to call all other functions and in doing so, play the game of rock, paper, scissors
        while self.computer_wins < 2 and self.user_wins < 2:      # While loop that runs the game until three rounds have been played 
            input("\nPress Enter to play the round whenever you are ready ")    # Asks user if they're ready to play the round
            
            # Prints "Best out of three" after the first round
            if self.computer_wins + self.user_wins == 0:
                pass
            else:
                print("\nBest out of three to win the game!")

            # 3 second Countdown before the start of a round (prints each number only once)
            start_time = time.time()
            x = 0
            while (time.time() - start_time) < 3:
                if round(time.time() - start_time) == 1 and x == 0: x = 1; print(3) 
                elif round(time.time() - start_time) == 2 and x == 1: x = 2; print(2)
                elif round(time.time() - start_time) == 3 and x == 2: x = 3; print(1)
                elif round(time.time() - start_time) == 4 and x == 3: print(0)
            
            # Calls functions to play the game 
            self.get_computer_choice()
            self.get_user_choice()
            self.get_winner(self.computer_choice, self.user_choice)

        # Checks whether anyone has won the game yet by accumulating 2 wins and, if so, ends the image capture
        if self.computer_wins >= 2 or self.user_wins >= 2:
            print(f"The {self.winner} won this game!\n") 
            cap.release()           # After the loop release the cap object - Ends image capture
            cv2.destroyAllWindows() # Destroy all the windows - Ends image capture
        

rps = RockPaperScissors()
rps.play()