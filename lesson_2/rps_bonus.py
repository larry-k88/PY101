import random
import os

OPTIONS_DICT = {
                'r' : 'rock',
                'p' : 'paper',
                's' : 'scissors',
                'l' : 'lizard',
                'sp' : 'spock',
            }

OPTIONS_ABBREVIATED = list(OPTIONS_DICT.keys())

WINNING_OUTCOMES = {
                'r' : ['s', 'l'],
                'p' : ['r', 'sp'],
                's' : ['p', 'l'],
                'l' : ['p', 'sp'],
                'sp' : ['r', 's'],
                }

os.system('clear')

def prompt(message):
    print(f'==> {message}')

def display_welcome():
    prompt('Welcome to Rock, Paper, Scissors, Lizard, Spock!')

def display_options():
    for k, v in OPTIONS_DICT.items():
        print(f'{k} for {v}')

def decide_winner(player, computer):
    prompt(f'You chose: {OPTIONS_DICT.get(player)}, '
           f'computer chose: {OPTIONS_DICT.get(computer)}')
    if computer in WINNING_OUTCOMES[player]:
        return 'player_wins'
    if player in WINNING_OUTCOMES[computer]:
        return 'computer_wins'
    return 'tie'

def display_winner(winner):
    match winner:
        case 'player_wins':
            prompt('You win!')
        case 'computer_wins':
            prompt('Computer wins!')
        case 'tie':
            prompt('It\'s a tie!')

display_welcome()
while True:
    prompt('To make your choice, type one of the following:')
    display_options()
    user_choice = input('Select an option: ').casefold()

    while user_choice not in OPTIONS_ABBREVIATED:
        prompt("That's not a valid choice")
        user_choice = input('Select an option: ').casefold()

    computer_choice = random.choice(OPTIONS_ABBREVIATED)

    who_wins = decide_winner(user_choice, computer_choice)

    display_winner(who_wins)

    while True:
        prompt('Do you want to play again? y/n')
        play_again = input().casefold()

        if play_again not in ['y', 'n']:
            prompt('Please enter y or n...')
            play_again = input().casefold()

        else:
            break

    if play_again == 'n':
        break
    os.system('clear')