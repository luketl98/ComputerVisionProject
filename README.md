# ComputerVisionProject
A program that will allow the user to play Rock, Paper, Scissors using just their webcam

After creating and cloning my GitHub repository and linking it to VSCode;

First I went to TeachableMachine, selected create a new image model and created four classes named 'Rock', 'Paper', 'Scissor' and 'Nothing'

I used 200-300 image samples for each class and trained the model, then I breifly tested the model using the preview funciton on the TeachableMachine website to check it was working to a sufficient standard - I'll update the model if I feel it necessary later on in the project

I exported the model and saved it locally, then added it to my GitHub repo and pulled the changes to the project folder through VSCode

Following this, I used a test file(model_checking_file.py) to check that the data was correctly stored and all the necessary files, packages and libraries were installed correctly and in the right place, I created a requirements.txt via Conda.

I then started on the code that would store the users and the computers choices during the game, I created a manual version of the Rock, Paper, Scissors (RPS) game that would allow the user to play RPS without the use of the camera, instead, by just using the keyboard to select their choice.
I created two seperate functions, get_computer_choice, and get_user_choice, first to generate the computers choice using the random module and a list containing the possible choices. Then  get_user_choice to attain the users choice using the input funtion and if statements.









