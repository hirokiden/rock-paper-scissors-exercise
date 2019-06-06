# game.py

# print("Rock, Paper, Scissors, Shoot!")

# Activate the following python

# conda create -n game-env python=3.7 # (first time only)
# conda activate game-env

# pip install pytest  --> install pytest package

# python game.py --> command line



# Modules/Packages that you need to import
import random


# CAPTURE INPUTS

potential_choice = ["rock", "paper", "scissors"]

user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

print("--------------")
print("USER CHOICE:", user_choice)

# VALIDATE INPUTS


if user_choice not in potential_choice:
    print("INVALID SELECTION, PLEASE TRY AGAIN...")
    exit()



# GENERATE COMPUTER SELECTION



pc_random_choice = random.choice(potential_choice)

print("--------------")
print("GENERATING...")
print("PC CHOICE:", pc_random_choice)


# DETERMINE THE WINNER

if user_choice == pc_random_choice:
    print("The Game is a tie")
elif user_choice == "rock" and pc_random_choice == "paper":
    print("Paper is the winner, you lose")
elif user_choice == "paper" and pc_random_choice == "scissors":
    print("Scissors is the winner, you lose")
elif user_choice == "scissors" and pc_random_choice == "rock":
    print("Rock is the winner, you lose")
elif user_choice == "rock" and pc_random_choice == "scissors":
    print("Rock is the winner, you win")
elif user_choice == "paper" and pc_random_choice == "rock":
    print("Paper is the winner, you win")
elif user_choice == "scissors" and pc_random_choice == "paper":
    print("Scissors is the winner, you win")

# Rock beats scissors
# Paper beats Rock
# Scissors beats Paper 
# Same selection is a tie


# DISPLAY FINAL OUTPUTS / OUTCOMES