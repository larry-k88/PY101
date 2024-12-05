# Ask user which operation they want to perform
# Perform the operation on the 2 inputs
# Print the result (and the operation?) to the terminal

print('Welcome to Calculator: choose two numbers and an operation to perform!')

# Ask user for two numbers
print('What is the first number?')
number_1 = input()
print('What is the second number?')
number_2 = input()

print(f'You chose {number_1} and {number_2}')

print('What operation would you like to perform?\n1) Add 2) Subtract '
      '3) Multiply 4) Divide')
operation = input()

if operation == '1':
    output = int(number_1) + int(number_2)
elif operation == '2':
    output = int(number_1) - int(number_2)
elif operation == '3':
    output = int(number_1) * int(number_2)
elif operation == '4':
    output = int(number_1) / int(number_2)
print(f'The result is {output}')