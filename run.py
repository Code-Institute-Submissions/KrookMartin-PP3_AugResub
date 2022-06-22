# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

def menu():
    print('[1] Rock/Paper/Scissors')
    print('[2] option 2')
    print('[3] option 3')
    print('[0] end program')


menu()


option = int(input('Enter the number of the game you want to play '))
while option != 0:
    if option == 1:

        player_score = 0
        computer_score = 0
        choices = ['rock', 'paper', 'scissors']

        while True:
            p_choice = input('Rock/Paper/Scissors or E to end: ').lower()
            if p_choice == "e":
                break
            if p_choice not in choices:
                continue

            random_choice = random.randint(0, 2)

            computer_choice = choices[random_choice]
            print("The computer's choice was", computer_choice)

            if p_choice == 'rock' and computer_choice == 'scissors':
                print('Plyers wins!')
                player_score += 1

            elif p_choice == 'paper' and computer_choice == 'rock':
                print('Plyers wins!')
                player_score += 1
            
            elif p_choice == 'scissors' and computer_choice == 'rock':
                print('Plyers wins!')
                player_score += 1
    
            else:
                print('You lost')
                computer_score += 1
            
        print('Final score player:', player_score)
        print('Final score computer:', computer_score)
        print('Thank you for playing, have a nice day!')
        menu()
#elif option == 1: