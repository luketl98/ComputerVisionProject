# ComputerVisionProject

A program that will allow the user to play Rock, Paper, Scissors using their webcam. For this project I created an Image model using TeachableMachine

## Setting up the environment

First I created and cloned my GitHub repository and linked it to VSCode.

## Computer vision model

I opened TeachableMachine, selected create a new image model and created four classes named 'Rock', 'Paper', 'Scissor' and 'Nothing'.

I used 200-300 image samples for each class and trained the model, then I breifly tested the model using the preview funciton on the TeachableMachine website to check it was working to a sufficient standard - I'll update the model if I feel it necessary later on in the project.

I exported the model and saved it locally, then added it to my GitHub repo and pulled the changes to the project folder through VSCode.

## Install Dependancies

Following this, I used a test file(model_checking_file.py) to check that the data was correctly stored and all the necessary files, packages and libraries were installed correctly and in the right place, I created a requirements.txt via Conda where the necessary libraries can be downloaded.

## Manual version Rock, Paper, Scissors

I began by creating a manual version of the Rock, Paper, Scissors (RPS) game that would allow the user to play RPS without the use of the camera, instead, by just using the keyboard to select their choice. I called this 'manual_rps'.

I created a class called 'rockpaperscissors' inside which, inside which I'll store all the functions I'll write for the game along with an __init__ with the variables. Creating a class meant I could use the same variables across different functions. I created an __init__ and defined some variables there and then mmoved on to the core of the program.

#### get_computer_choice() & get_user_choice() {manual_rps}
I created two seperate functions, get_computer_choice, and get_user_choice, the first to generate and store the computers choice using the random module and a list containing the possible choices. Then get_user_choice to attain and assign the users choice using the input funtion and if-elif-else statements.

#### get_winner() {manual_rps}
Then I created another function called 'get_winner' which takes the two arguments get_computer_choice, and get_user_choice. Then with the standard rules of rock, paper, scissors in mind I used if-elif-else statments to figure out whether the user of the computer was the winner or if the result was a tie. The program would then print the result on screen and add 1 to user_wins or computer_wins and finally print the current number of wins for both.

#### play() {manual_rps}
I then added a function called play() to run all three functions; get_computer_choice, get_user_choice and get_winner.

So now the play() function is called, which in turn calls the three other functions and begins the game. It asks the user for their choice and generates the computers choice, then prints boths choices and tells the user who won the round. 

I then added a while loop at the beginning of this function to check whether the user or computer had reached 2 wins yet before continuing with the game. If so, a message would be printed revealing who has won.

## Using the Camera to play

I created a new file called 'camera_rps.py' where I 
wrote the code that will allow the user to use the output of the computer vision system to play the game. This code will be a modified version of the manual_rps file.

#### get_prediction
A new function called get_predicition modifies the code from the model_checking_file to include a couple of things. 

First the numpy.argmax function. The data returned by the model is a list of four numbers equating to probabilities of each class(Rock, Paper, Scissors, Nothing) being shown. So the class with the highest value is the class that the model predicts is the one being shown to the camera. The numpy.argmax function takes the list of four and returns the element with the highest value, which will be a number, either 0, 1, 2 or 3. These numbers represent each class, being Rock, Paper, Scissors and Nothing assuming you used this order when making the model on Teachable Machine. I then used if statements to print whatever class that was returned, so the user could check that the model was correctly identifying their choice. I had some issues with the accuracy of the models prediction, where I had to fiddle around with my hands positioning in front of the camera before the model would correctly identify my choice. To resolve this issue slightly I added a 5 second timer, whilst silmultaneously printing the models prediction, to give the user some time to fiddle around with the positioning of their hand and make sure the model gets the prediction right. I will also redo and replace the model I currently have with an improved version later on, again using TeachableMachine but perhaps with more images per class.

#### play()
Within the play() function there is a countdown that counts to 3 before running the three required functions, this mimics the 3 second countdown you would normally have before revealing your choice when playing a game of Rock, Paper, Scissors. The time.sleep() function could not be used in this instance as 

I also added an input just before the countdown starts, requiring the user to press Enter to ensure the user is ready for the countdown the begin.

At the end of play() the else statement checks if the number of wins accumulated by the user and computer has reached 2, in which case the winner will be printed and cap.release() and cv2.destroyAllWindows() will be run to end the image capture. These two functions were originally part of the model_cehcking_file, but were moved to this function so they would only be called once game was completely finished as opposed to at the end of each round.


## Potential improvements

Certain aspects of the code could be simplified but at possibly at a cost of clarity and readability - This is still something I would like to look at in future though. As an example, the self.rock, self.paper etc. variables could be removed and replaced simply by the numbers returned by the numpy.argmax function, being 0,1,2 and 3. With code related to the four classes being modified and again simplified too.

The countdown could also be more elegant that it currently is. The print function could be removed entirely which would reduce its length to a couple of lines only. 

If the model can be trained to a sufficient standard where it can accurately predict the class chosen by the user, the image capture would not have to be run for 5 seconds nor would the result have to be printed inside  get_prediction(). 

Ideally the image capture popup would contain the printed messages, which could be another feature to add in future too.



