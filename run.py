# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


def menu():
    """Askign user to select a game to play """
    print('[1] Rock/Paper/Scissors')
    print('[2] Know your Nintendo')
    print('[3] option 3')
    print('[0] end program')


menu()


def rpsgame():
    player_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']

    p_choice = input('Rock/Paper/Scissors or E to end: ').lower()
    if p_choice == "e":
        print('Final score player:', player_score)
        print('Final score computer:', computer_score)
        print('Thank you for playing, have a nice day!')
        menu()
    elif p_choice in choices:
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
    else:
        print('Please enter rock/papper or scissor')
                
    #print('Final score player:', player_score)
    #print('Final score computer:', computer_score)
    #print('Thank you for playing, have a nice day!')
    #menu()


def quiz():
    print('Welcome to know your Nintendo')
    start_game = input('Start game? yes/no?')
    if start_game != 'yes':
        print('goodbye!')
        menu()
    else:
        print('Game on!')

        question = input('Whats the name of Super Marios brother?')
        if question == 'Luigi':
            print('Correct')
        else: 
            print('Incorrect')     

    question = input('What is the name of the protagonist in Metal Gear?')
    if question == 'Snake':
        print('Correct')
    else: 
        print('Incorrect')     

    question = input('What is the name of Super Marios nemesis?')
    if question == 'Bowser':
        print('Correct')
    else: 
        print('Incorrect')     

    question = input('What is the name of the protagonist in Zelda?')
    if question == 'Link':
        print('Correct')
    else:
        print('Incorrect')
        
    question = input('What color is the original megaman?')
    if question == 'Blue':
        print('Correct')
    else:
        print('Incorrect')


def game_selector():
    option = int(input('Enter the number of the game you want to play '))
    while option != 0:
        if option == 1:
            rpsgame()
        elif option == 2:
            quiz()


game_selector()