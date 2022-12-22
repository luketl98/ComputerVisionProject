# ComputerVisionProject
A program that will allow the user to play Rock, Paper, Scissors using just their webcam

**Set up environment**
First I created and cloned my GitHub repository and linked it to VSCode;

**Computer vision model**
I went to TeachableMachine, selected create a new image model and created four classes named 'Rock', 'Paper', 'Scissor' and 'Nothing'

I used 200-300 image samples for each class and trained the model, then I breifly tested the model using the preview funciton on the TeachableMachine website to check it was working to a sufficient standard - I'll update the model if I feel it necessary later on in the project

I exported the model and saved it locally, then added it to my GitHub repo and pulled the changes to the project folder through VSCode

**Install Dependancies**
Following this, I used a test file(model_checking_file.py) to check that the data was correctly stored and all the necessary files, packages and libraries were installed correctly and in the right place, I created a requirements.txt via Conda where the necessary libraries can be downloaded

**Manual version Rock, Paper, Scissors**
I then created a manual version of the Rock, Paper, Scissors (RPS) game that would allow the user to play RPS without the use of the camera, instead, by just using the keyboard to select their choice, I called this 'manual_rps'.

I created a class called 'rockpaperscissors' inside which, I will put all the functions I will write for the game, this was so I could use the same variables across different functions. I created an __init__ and defined some variables there and then mmoved on to the core of the program.

I created two seperate functions, get_computer_choice, and get_user_choice, first to generate and store the computers choice using the random module and a list containing the possible choices. Then get_user_choice to attain and store the users choice using the input funtion and if-elif-else statements.

Then I created another function called 'get_winner' which takes the two arguments get_computer_choice, and get_user_choice. Then with the standard rules of rock, paper, scissors in mind I used if-elif-else statments to figure out whether the user of the computer was the winner or if the result was a tie. The program would then print the result on screen.

I added a function called 'play' to run all three functions; get_computer_choice, get_user_choice and get_winner

So now the 'play' function is called which in turn calls the three other functions and begins the game. It asks the user for their choice and generates the computers choice, then prints boths choices and tells the user who won the game.

**Using the Camera to play**
I created a new file called 'camera_rps.py' where I will write the code that will allow the user to use the output of the computer vision system to play the game.



----------








