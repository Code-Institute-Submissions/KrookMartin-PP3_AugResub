# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

player_score = 0 
computer_score = 0
choices = ['rock', 'papper, scissors']

while True:
    player_choice = input('Rock/Papper/Scissors or E to end').lower()
    if player_choice == "e":
        break
    if player_choice not in choices:
        continue

        random_choice = random.randint(0, 2)


print('Thank you for playing, have a nice day!')