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


user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

print("--------------")
print("USER CHOICE:", user_choice)

# VALIDATE INPUTS


if user_choice not in ["rock", "paper", "scissors"]:
    print("INVALID SELECTION, PLEASE TRY AGAIN...")
    exit()



# GENERATE COMPUTER SELECTION



pc_list = ["rock", "paper", "scissors"]

pc_random_choice = random.choice(pc_list)

print("--------------")
print("GENERATING...")
print("PC CHOICE:", pc_random_choice)


# DETERMINE THE WINNER



# DISPLAY FINAL OUTPUTS / OUTCOMES