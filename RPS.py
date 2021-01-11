import random
import os


options =  ["Rock", "Paper", "Scissors"]


gameRunning = True

#Variables to keep track of score
playerScore = 0
compScore = 0


#loop through game
while gameRunning:

#prints out current score, input message and has the computer choose from options
	print(f"\nPlayer: {playerScore}\nComputer: {compScore}\n")

	choice = str(input("Rock[R]\nPaper[P]\nScissors[S]\nWhat will you choose? "))

	comp = random.choice(options)

#Checks players choice against computer choice and awards points to appropriate variable
	if choice.upper() == "R":
		if comp == options[0]:
			print("You both chose Rock! Try again!\n")
		elif comp == options[1]:
			compScore += 1
			print("Computer chose paper, You lose!\n")
		elif comp == options[2]:
			playerScore += 1
			print("Computer chose Scissors, You win!\n")

	elif choice.upper() == "P":
		if comp == options[0]:
			playerScore += 1
			print("Computer chose rock, You win!\n")
		elif comp == options[1]:
			print("Computer chose paper, You tie!\n")
		elif comp == options[2]:
			compScore += 1
			print("Computer chose scissors, You lose!\n")

	elif choice.upper() == "S":
		if comp == options[0]:
			compScore += 1
			print("Computer chose rock, You lose!\n")
		elif comp == options[1]:
			playerScore += 1
			print("Computer chose paper, You win!\n")
		elif comp == options[2]:
			print("Computer chose scissors, You tie!\n")

	else:
		print("Invalid input, please input the first letter of your choice")






