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

with open('rps_bonus_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'==> {message}')

def display_welcome():
    prompt(MESSAGES["welcome"])

def display_rules():
    prompt(MESSAGES['rules']['general'])
    prompt(MESSAGES['rules']['rock'])
    prompt(MESSAGES['rules']['paper'])
    prompt(MESSAGES['rules']['scissors'])
    prompt(MESSAGES['rules']['lizard'])
    prompt(MESSAGES['rules']['spock'])
    prompt(MESSAGES['start_game'])
    input()
    os.system('clear')

def display_options():
    for k, v in OPTIONS_DICT.items():
        print(f'{k} for {v}')

def display_current_scores():
    prompt(f'{MESSAGES['current_scores']}\n{get_scores()}')

def get_scores():
    return (f'Round: {scores['Round']}\n'
            f'You: {scores['Player']}\n'
            f'Computer: {scores['Computer']}')

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

def decide_winner_round(player, computer):
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
        case 'computer_wins':
            prompt(MESSAGES['computer_win_round'])
        case 'tie':
            prompt(MESSAGES['tie_round'])

def decide_winner_match():
    if scores['Computer'] == WINNING_SCORE:
        return 'computer_wins'
    if scores['Player'] == WINNING_SCORE:
        return 'player_wins'
    return None

def display_winner_match(winner):
    match winner:
        case 'player_wins':
            prompt(MESSAGES['player_win_match'])
        case 'computer_wins':
            prompt(MESSAGES['computer_win_match'])

def display_final_scores():
    prompt(f'{MESSAGES['final_scores']}\n{get_scores()}')
    print()

def display_end_game():
    prompt(f'{MESSAGES['quit']}\n{get_scores()}')

# Game starts here

os.system('clear')
display_welcome()
prompt(MESSAGES['view_rules'])
rules_or_play = input().casefold()
if rules_or_play == 'rules':
    display_rules()

scores = {'Player' : 0,
          'Computer' : 0,
          'Round': 0}
while True:
    prompt(MESSAGES['user_choice'])
    display_options()
    print()
    display_current_scores()
    print()

    user_choice = get_user_choice()
    computer_choice = random.choice(OPTIONS_ABBREVIATED)

    round_winner = decide_winner_round(user_choice, computer_choice)
    scores['Round'] += 1

    prompt(f'You chose: {OPTIONS_DICT.get(user_choice)}')
    prompt(f'Computer chose: {OPTIONS_DICT.get(computer_choice)}')

    display_winner_round(round_winner)

    match_winner = decide_winner_match()

    if match_winner:
        display_final_scores()
        display_winner_match(match_winner)
        break

    prompt(MESSAGES['play_again'])
    play_again = input().casefold()

    if play_again == 'exit':
        print()
        display_end_game()
        break

    os.system('clear')