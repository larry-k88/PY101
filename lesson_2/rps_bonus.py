import random
import os
import json

OPTIONS_DICT = {
                'r' : 'rock',
                'p' : 'paper',
                'sc' : 'scissors',
                'l' : 'lizard',
                'sp' : 'spock',
            }

OPTIONS_ABBREVIATED = list(OPTIONS_DICT.keys())

WINNING_OUTCOMES = {
                'r' : ['sc', 'l'],
                'p' : ['r', 'sp'],
                'sc' : ['p', 'l'],
                'l' : ['p', 'sp'],
                'sp' : ['r', 'sc'],
                }

WINNING_SCORE = 3

def prompt(message):
    print(f'==> {message}')

def display_welcome():
    prompt(MESSAGES["welcome"])

def display_rules():
    prompt(MESSAGES['view_rules'])
    rules = input().casefold()
    if rules == 'rules':
        print()
        prompt(MESSAGES['rules']['general'])
        print()
        prompt(MESSAGES['rules']['rock'])
        prompt(MESSAGES['rules']['paper'])
        prompt(MESSAGES['rules']['scissors'])
        prompt(MESSAGES['rules']['lizard'])
        prompt(MESSAGES['rules']['spock'])
        print()
        prompt(MESSAGES['start_game'])
        input()
    os.system('clear')

def display_options():
    for k, v in OPTIONS_DICT.items():
        print(f'{k} for {v}')

def decide_winner_round(player, computer):
    prompt(f'You chose: {OPTIONS_DICT.get(player)}')
    prompt(f'Computer chose: {OPTIONS_DICT.get(computer)}')
    print()
    if computer in WINNING_OUTCOMES[player]:
        scores['Player'] += 1
        return 'player_wins'
    if player in WINNING_OUTCOMES[computer]:
        scores['Computer'] += 1
        return 'computer_wins'
    return 'tie'

def display_winner_round(winner):
    match winner:
        case 'player_wins':
            prompt(MESSAGES['player_win_round'])
            print()
        case 'computer_wins':
            prompt(MESSAGES['computer_win_round'])
            print()
        case 'tie':
            prompt(MESSAGES['tie_round'])
            print()

def decide_winner_match():
    if scores['Computer'] == WINNING_SCORE:
        return 'computer_wins'
    if scores['Player'] == WINNING_SCORE:
        return 'player_wins'
    return None

def display_winner_match(winner):
    match winner:
        case 'player_wins':
            display_final_scores()
            print()
            prompt(MESSAGES['player_win_match'])
        case 'computer_wins':
            display_final_scores()
            print()
            prompt(MESSAGES['computer_win_match'])

def get_scores():
    return (f'You: {scores['Player']} \nComputer: {scores['Computer']}')

def display_current_scores():
    prompt(f'{MESSAGES['current_scores']}\n{get_scores()}')

def display_final_scores():
    prompt(f'{MESSAGES['final_scores']}\n{get_scores()}')

def get_user_choice():
    prompt(MESSAGES['user_prompt'])
    user_input = input().casefold()

    while user_input not in OPTIONS_ABBREVIATED:
        if user_input == 's':
            prompt(MESSAGES['scissors_or_spock'])
        else:
            prompt(MESSAGES['invalid_choice'])
        user_input = input().casefold()
    return user_input

def display_end_game():
    os.system('clear')
    display_final_scores()
    print()
    prompt(MESSAGES['thanks'])

with open('rps_bonus_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Game starts here

os.system('clear')
display_welcome()
print()
display_rules()
print()

scores = {'Player' : 0,
          'Computer' : 0}
while True:
    prompt(MESSAGES['user_choice'])
    display_options()
    print()
    display_current_scores()
    print()

    user_choice = get_user_choice()
    computer_choice = random.choice(OPTIONS_ABBREVIATED)

    round_winner = decide_winner_round(user_choice, computer_choice)
    display_winner_round(round_winner)

    match_winner = decide_winner_match()
    display_winner_match(match_winner)

    if match_winner:
        break

    prompt(MESSAGES['play_again'])
    play_again = input().casefold()

    if play_again == 'exit':
        display_end_game()
        break

    os.system('clear')