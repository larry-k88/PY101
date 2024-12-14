# Ask user which operation they want to perform
# Perform the operation on the 2 inputs
# Print the result (and the operation?) to the terminal

# Pseudocode

# Ask user for 2 numbers
# Ask user which operation to use
# Perform operation depending on choice
# Print result

# Formal pseudocode

# START
# GET number_1 and number_2
# SET number_1 and number_2
# GET operation
# IF operation = 1 of 4 options:
#   Perform that operation
# PRINT the result
# END

import json

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def messages(message):
    return data[lang][message]

with open('calculator_messages.json', 'r') as file:
    data = json.load(file)

prompt(data['welcome'])

while True:
    lang = 'en'
    lang_choice = input()
    if lang_choice == '1':
        break
    elif lang_choice == '2':
        lang = 'fr'
        break
    else:
        prompt(data['language'])

while True:
    prompt(messages('first_number'))
    number1 = input()

    while invalid_number(number1):
        prompt(messages('number_input_error'))
        number1 = input()

    prompt(messages('second_number'))
    number2 = input()

    while invalid_number(number2):
        prompt(messages('number_input_error'))
        number2 = input()

    prompt(messages('operation'))
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(messages('operation_input_error'))
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)
    output = round(output, 2)

    prompt(f'{messages('output')}{output}')

    prompt(messages('carry_on'))
    carry_on = input()
    if carry_on not in ['Y', 'y', 'yes']:
        break
        