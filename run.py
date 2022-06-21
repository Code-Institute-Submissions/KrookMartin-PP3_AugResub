# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

player_score = 0
computer_score = 0
choices = ['rock', 'paper', 'scissors']

while True:
    player_choice = input('Rock/Paper/Scissors or E to end' + ':').lower()
    if player_choice == "e":
        break
    if player_choice not in choices:
        continue

    random_choice = random.randint(0, 2)

    computer_choice = choices[random_choice]
    print("The computer's choice was", computer_choice)

    if player_choice == 'rock' and computer_choice == 'scissors':
        print('Plyers wins!')
        player_score += 1

    elif player_choice == 'paper' and computer_choice == 'rock':
        print('Plyers wins!')
        player_score += 1
           
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print('Plyers wins!')
        player_score += 1
  
    else:
        print('You lost')
        computer_score += 1
        
print('Final score player:', player_score)
print('Final score computer:', computer_score)
print('Thank you for playing, have a nice day!')
