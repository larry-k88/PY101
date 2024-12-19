'''
Problem:    Build a mortgage calculator to determine monthly payments
            Input - loan amount, APR, loan duration
            Output - monthly payments with units

Examples/Test Cases:    Loan amount = £12,000        
                        APR = 7%
                        Loan Duration = 5 years
                        Monthly payments = £237.61

Data:                   input() x 3
                        Assign to 3 variables
                        Arithmetic operators
                        print()                         

Algorithm:  

    Pseudocode

        Ask user for 3 numbers
        Assign variables to the inputs
        Perform calculation
        Print in 

    Formal pseudocode

        START
        GET loan_value
        GET apr
        GET loan_duration
        SET x3
        Convert to correct units/types
        Perform the calculation
        PRINT the result
        END
'''
def prompt(message):
    print(f'--> {message}')

def invalid_number_type(number_str):
    try:
        float(number_str)
    except (ValueError, TypeError):
        return True
    if number_str.startswith('-'):
        return True
    return False

def display_welcome():
    prompt('Welcome to the Repayment Calculator!')

def display_monthly_payments():
    prompt(f'Your monthly repayments will be: £{output_monthly_payments:.2f}')

def get_carry_on():
    prompt('Do you want to do another calculation? (y/n)')
    carry_on = input()
    while carry_on not in ['n', 'N', 'no', 'No', 'y', 'Y', 'yes', 'Yes']:
        prompt('Please enter y or n')
        carry_on = input()
        if carry_on in ['y', 'Y', 'yes', 'Yes']:
            return True
        if carry_on in ['n', 'N', 'no', 'No']:
            return False

def get_loan_amount():
    prompt('What is the loan amount?')
    loan_amount_string = input()
    while invalid_number_type(loan_amount_string):
        prompt('Please provide a positive whole number or decimal')
        loan_amount_string = input()
    return loan_amount_string

def get_apr():
    prompt('What is the APR as a percentage?')
    monthly_apr_string = input()
    while invalid_number_type(monthly_apr_string):
        prompt('Please provide a positive whole number or decimal')
        monthly_apr_string = input()
    return monthly_apr_string

def get_loan_duration():
    prompt('What is the loan duration in years?')
    loan_duration_string = input()
    while invalid_number_type(loan_duration_string):
        prompt('Please provide a positive whole number or decimal')
        loan_duration_string = input()
    return loan_duration_string

def calc_monthly_payments():
    loan_amount_float = float(get_loan_amount())
    monthly_apr_float = float(get_apr()) / 100 # converts percentage to decimal
    annual_apr_float = monthly_apr_float / 12
    loan_duration_float = float(get_loan_duration()) * 12 # converts to months

    try:
        monthly_payments = (loan_amount_float * annual_apr_float
                        / (1 - (1 + annual_apr_float)
                        ** (-loan_duration_float)))
    except ZeroDivisionError:
        monthly_payments = loan_amount_float / loan_duration_float
    return monthly_payments

display_welcome()
while True:
    output_monthly_payments = calc_monthly_payments()
    display_monthly_payments()
    if not get_carry_on():
        prompt('Thank you for using the Repayment Calculator!')
        break
    