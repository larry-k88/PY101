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

print('Welcome to Calculator: choose two numbers and an operation to perform!')

# Ask user for two numbers
print('What is the first number?')
number_1 = int(input())
print('What is the second number?')
number_2 = int(input())

print(f'You chose {number_1} and {number_2}')

print('What operation would you like to perform?\n1) Add 2) Subtract '
      '3) Multiply 4) Divide')
operation = input()

if operation == '1':
    output = number_1 + number_2
elif operation == '2':
    output = number_1 - number_2
elif operation == '3':
    output = number_1 * number_2
elif operation == '4':
    output = number_1 / number_2
print(f'The result is {output}')