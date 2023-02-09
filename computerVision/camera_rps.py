import random
# --- model_copy.py imports etc. :
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


    def get_computer_choice(self): # Function to get the computers choice by randomly selecting from list
        # list containing possible choices
        game_options = ["Rock", "Paper", "Scissors"]
        # randomly selects choice from list and assigns it to variable
        self.computer_choice = random.choice(game_options)
        # returns the computers choice
        return self.computer_choice


    def get_user_choice(self): 
        self.user_choice = rps.get_prediction()

        if self.user_choice == 0:
            self.user_choice = self.rock
            print(f"\nYou chose: {self.user_choice}\n")

        elif self.user_choice == 1:
            self.user_choice = self.paper
            print(f"\nYou chose: {self.user_choice}\n")

        elif self.user_choice == 2:
            self.user_choice = self.scissors
            print(f"\nYou chose: {self.user_choice}\n")

        elif self.user_choice == 3:
            self.user_choice = self.nothing
            print(f"\nYou chose: {self.nothing}, please try again!\n")
            rps.play()

        return self.user_choice

    def get_winner(self, computer_choice, user_choice): # Function to take the choices of the user and computer and return the result of the game

    # prints the computers choice
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
        

    def get_prediction(self): # Function to start the image capture and classify results 

        start_time = time.time()  # Time at beginning of program - Used for the countdown within get_prediction function
        
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
                    
            # Assign the result
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

            # Countdown
            if (time.time() - start_time) < 7:
                print(round((start_time - time.time())*(-1)))
            elif (time.time() - start_time) > 7:
                break
            else:
                pass

            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            
        # After the loop release the cap object
        cap.release()

        # Destroy all the windows
        cv2.destroyAllWindows()

        # Reprint the final result 007
        # print("Final result: ", result)

        # Return the result 
        return result



rps = rockpaperscissors()
rps.play()