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

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt('Welcome to Calculator: '
       'choose two numbers and an operation to perform!')

# Ask user for two numbers
prompt('What is the first number?')
number_1 = input()

while invalid_number(number_1):
    prompt("That doesn't look like a valid number.")
    number_1 = input()

prompt('What is the second number?')
number_2 = input()

while invalid_number(number_2):
    prompt("That doesn't look like a valid number.")
    number_2 = input()

prompt(f'You chose {number_1} and {number_2}')

prompt('What operation would you like to perform?\n1) Add 2) Subtract '
      '3) Multiply 4) Divide')
operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt("You must choose 1, 2, 3 or 4")
    operation = input()

match operation:
    case '1':
        output = int(number_1) + int(number_2)
    case '2':
        output = int(number_1) - int(number_2)
    case '3':
        output = int(number_1) * int(number_2)
    case '4':
        output = int(number_1) / int(number_2)

prompt(f'The result is {output}')
