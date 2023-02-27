import random
# --- model_copy.py imports :
import time
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

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



    def get_user_choice(self): # Determines the users choice via image capture 
        # Calls get_prediction and starts image capture to determine users choice
        self.user_choice = rps.get_prediction()
        # assign numpy.argmax result to a class and print 
        if self.user_choice == 0:
            self.user_choice = self.rock
            print(f"\nYou chose Rock\n")
        elif self.user_choice == 1:
            self.user_choice = self.paper
            print(f"\nYou chose Paper\n")
        elif self.user_choice == 2:
            self.user_choice = self.scissors
            print(f"\nYou chose Scissors\n")
        elif self.user_choice == 3:
            print(f"\nYou chose Nothing, please try again!\n")
            rps.play()

        return self.user_choice
    # End of get_user_choice()

    def get_winner(self, computer_choice, user_choice): # Function to take the choices of the user and computer and return the result of the game

    # prints the computers choice
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
        # While loop that runs the game until three rounds have been played 
        while self.computer_wins != 2 and self.user_wins != 2:
            # Asks user if they're ready to play the round
            input("\nPress Enter to play the round whenever you are ready ").lower
            
            # Prints 
            if self.computer_wins + self.user_wins == 0:
                pass
            else:
                print("\nBest out of three to win the game!")

            # 3 second Countdown before the start of a round
            start_time = time.time()
            x = 0
            while (time.time() - start_time) < 3:
                if round(time.time() - start_time) == 1 and x == 0: x = 1; print(3) 
                elif round(time.time() - start_time) == 2 and x == 1: x = 2; print(2)
                elif round(time.time() - start_time) == 3 and x == 2: x = 3; print(1)
                elif round(time.time() - start_time) == 4 and x == 3: print(0)
            
            # Calls functions to play the game 
            rps.get_computer_choice()
            rps.get_user_choice()
            rps.get_winner(rps.computer_choice, rps.user_choice)

        # Checks whether anyone has won the game yet by accumulating 2 wins and, if so, ends the image capture
        else:
            if self.computer_wins == 2:
                print("You lost this game, the Computer wins!\n")
                # After the loop release the cap object - Ends image capture 
                cap.release()
                # Destroy all the windows - Ends image capture
                cv2.destroyAllWindows()
            elif self.user_wins == 2:
                print("You won the game!\n")
                # After the loop release the cap object - Ends image capture
                cap.release()
                # Destroy all the windows - Ends image capture
                cv2.destroyAllWindows()
    # End of play()

    def get_prediction(self): # Function to start the image capture and classify results 

        start_time = time.time()  # Time at beginning of program - Used for the countdown below
        
        while True:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data, verbose=0)
            # Point between start of program and start of image capture
            cv2.imshow('frame', frame)

            # Find the result using numpy
            result = np.argmax(prediction)

            """        
            # Print the result
            if result == 0:
                print("Rock")
            elif result == 1:
                print("Paper")
            elif result == 2:
                print("Scissors")
            elif result == 3:
                print("Nothing")
            else:
                pass
            
            # Makes the image capture run for 5 seconds before capturing the users choice 
            if (time.time() - start_time) < 5:
                pass
            elif (time.time() - start_time) > 5:
                break
            else:
                pass
            """

            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            break

        # Return the result 
        return result



rps = rockpaperscissors()
rps.play()