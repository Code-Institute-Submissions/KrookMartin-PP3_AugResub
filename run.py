import random


def rpsgame():
    """randomly picks rock paper scissors againt player"""

    player_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']

    while True:
        p_choice = input('Rock/Paper/Scissors or E to end: \n').lower()
        if p_choice == "e":
            break

        if p_choice not in choices:
            print('invalid option, please enter rock, paper or scissors')
            continue

        random_choice = random.randint(0, 2)
        computer_choice = choices[random_choice]
        print("The computer's choice was", computer_choice)

        if p_choice == 'rock' and computer_choice == 'scissors':
            print('Player wins!')
            player_score += 1

        elif p_choice == 'paper' and computer_choice == 'rock':
            print('Player wins!')
            player_score += 1

        elif p_choice == 'scissors' and computer_choice == 'rock':
            print('Player wins!')
            player_score += 1

        elif p_choice == computer_choice:
            print('draw')

        else:
            print('You lost')
            computer_score += 1

    print('Final score player:' + str(player_score))
    print('Final score computer:' + str(computer_score))
    print('Thank you for playing, have a nice day!')
    menu()


def quiz():
    """Quiz game that ask for user inputs in form of answers"""
    print('Welcome to know your Nintendo')
    start_game = input('Start game? yes/no? \n')
    score = 0
    if start_game.lower() != 'yes':
        print('goodbye!')
        menu()
    else:
        print('Game on!')
        question = input('Whats the name of Super Marios brother? \n')
        if question.lower() == 'luigi':
            score += 1
            print('Correct')
        else:
            print('Incorrect, the correct answer is luigi')

        question = input('What is the name of the hero in Metal Gear? \n')
        if question.lower() == 'snake':
            score += 1
            print('Correct')
        else:
            print('Incorrect, the correct answer is snake')

        question = input('What is the name of Super Marios nemesis? \n')
        if question.lower() == 'bowser':
            score += 1
            print('Correct')
        else:
            print('Incorrect, the correct answer is bowser')

        question = input('What is the name of the protagonist in Zelda? \n')
        if question.lower() == 'link':
            score += 1
            print('Correct')
        else:
            print('Incorrect, the correct answer is link')

        question = input('What color is the original megaman? \n')
        if question.lower() == 'blue':
            score += 1
            print('Correct')
        else:
            print('Incorrect, the correct answer is blue')

    print('Thanks for playing you got ' + str(score) + ' points')
    menu()


def magic_ball():
    """function to let player ask random question and get a random answer"""
    answer = ['Yes!', 'No', 'Maybe', 'Think about it i must', 'It depends']
    print('Ask the Magic 8Ball?')
    while str(input('Press enter to start or no to exit \n')).lower() != 'no':
        str(input('What is your question? \n'))

        random_answer = answer[random.randint(0, len(answer) - 1)]
        print(random_answer)
        print('Ask the Magic 8Ball another question?')

    print("Good Bye")
    menu()


def game_selector():
    """function to let player choose game or exit application"""
    option = (input('Enter the letter of the game you want to play \n'))
    option = option.lower()
    selector = ['a', 'b', 'c', 'q']
    while option.lower() not in selector:
        print('invalid input, please enter a,b,c or q')
        menu()

    if option == 'q':
        quit()
    elif option == 'a':
        rpsgame()
    elif option == 'b':
        quiz()
    elif option == 'c':
        magic_ball()


def menu():
    """Askign user to select a game to play """
    print('Welcome to the low-tech time killer')
    print('[a] Rock/Paper/Scissors')
    print('[b] Know your Nintendo')
    print('[c] Magic eightball')
    print('[q] end program')
    game_selector()


menu()
