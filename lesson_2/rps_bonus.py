import random
import os

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

os.system('clear')
def prompt(message):
    print(f'==> {message}')

def display_winner(player, computer):
    prompt(f'You chose: {player}, computer chose: {computer}')
    if (
        (player == 'rock' and computer == 'scissors') or
        (player == 'rock' and computer == 'lizard') or
        (player == 'paper' and computer == 'rock') or
        (player == 'paper' and computer == 'spock') or
        (player == 'scissors' and computer == 'paper') or
        (player == 'scissors' and computer == 'lizard') or
        (player == 'lizard' and computer == 'spock') or
        (player == 'lizard' and computer == 'paper') or
        (player == 'spock' and computer == 'scissors') or
        (player == 'spock' and computer == 'rock')
    ):
        return 'You win!'
    elif (
            (player == 'rock' and computer == 'paper') or
            (player == 'rock' and computer == 'spock') or
            (player == 'paper' and computer == 'scissors') or
            (player == 'paper' and computer == 'lizard') or
            (player == 'scissors' and computer == 'rock') or
            (player == 'scissors' and computer == 'spock') or
            (player == 'lizard' and computer == 'rock') or
            (player == 'lizard' and computer == 'scissors') or
            (player == 'spock' and computer == 'paper') or
            (player == 'spock' and computer == 'lizard')
    ):
        return 'Computer wins!'
    else:
        return 'It\'s a tie!'

while True:
    prompt(f'Choose one: {', '.join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(display_winner(choice, computer_choice))

    while True:
        prompt('Do you want to play again? y/n')
        play_again = input().lower()

        if play_again in ['y', 'n']:
            break
        else:
            prompt('Please enter y or n...')
    if play_again[0] == 'n':
        break

'''
Lines 23-44 can be replaced by the below, removing the need to have a
break statement (as per Q3 on Assignment 26)

keep_running = True
while keep_running:
    prompt(f'Choose one: {', '.join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(display_winner(choice, computer_choice))

    prompt('Do you want to play again? y/n')
    play_again = input().lower()
    while play_again not in ['y', 'n']:
        prompt('Please enter y or n...')
        play_again = input().lower()

    if play_again == 'n':
        keep_running = False
'''