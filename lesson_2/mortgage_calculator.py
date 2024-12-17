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

def invalid_number(number_str):
    try:
        float(number_str)
        if float(number_str) < 0:
            return True
    except ValueError:
        return True
    return False

def repayment_calc():
    return f'Your monthly repayments will be: £{monthly_payments:.2f}'

def get_loan_amount():
    prompt('What is the loan amount?')
    user_loan_amount = input()
    while invalid_number(user_loan_amount):
        prompt('Number must be greater than 0 and '
               'a whole number or decimal only')
        user_loan_amount = input()
    return user_loan_amount

def get_apr():
    prompt('What is the APR as a percentage?')
    user_apr = input()
    while invalid_number(user_apr):
        prompt('Number must be greater than 0 and '
               'a whole number or decimal only')
        user_apr = input()
    return user_apr

def get_loan_duration():
    prompt('What is the loan duration in years?')
    user_loan_duration = input()
    while invalid_number(user_loan_duration):
        prompt('Number must be greater than 0 and '
               'a whole number or decimal')
        user_loan_duration = input()
    return user_loan_duration

calc_loan_amount = float(get_loan_amount())
apr = float(get_apr()) / 12 / 100
calc_loan_duration = float(get_loan_duration()) * 12

monthly_payments = (calc_loan_amount
                    * apr / (1 - (1 + apr) ** (-calc_loan_duration)))

prompt(repayment_calc())
