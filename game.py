# game.py

# print("Rock, Paper, Scissors, Shoot!")

# Activate the following python

# conda create -n game-env python=3.7 # (first time only)
# conda activate game-env

# pip install pytest  --> install pytest package

# python game.py --> command line





# CAPTURE INPUTS


user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

print("--------------")
print("USER CHOICE:", user_choice)

# VALIDATE INPUTS


if user_choice not in ["rock", "paper", "scissors"]:
    print("INVALID SELECTION, PLEASE TRY AGAIN...")
    exit()



# GENERATE COMPUTER SELECTION

print("GENERATING...")

# DETERMINE THE WINNER

# DISPLAY FINAL OUTPUTS / OUTCOMES