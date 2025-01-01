import os

MONTHS_IN_YEAR = 12

def prompt(message):
    print(f'--> {message}')

def display_welcome():
    prompt('Welcome to the Repayment Calculator!')

def invalid_number_float(number_str):
    try:
        float(number_str)
    except (ValueError, TypeError):
        return True
    if float(number_str) < 0:
        return True
    if number_str.lower() in ['inf', 'nan']:
        return True
    return False

def invalid_number_int(number_str):
    try:
        int(number_str)
    except (ValueError, TypeError):
        return True
    if int(number_str) < 0:
        return True
    if number_str.lower() in ['inf', 'nan']:
        return True
    return False

def get_loan_amount():
    prompt('What is the loan amount (without the currency unit)?')
    loan_amount_string = input()
    if ',' in loan_amount_string:
        loan_amount_string = loan_amount_string.replace(',','')
    while (invalid_number_float(loan_amount_string)
           or loan_amount_string == '0'):
        prompt('Please provide a positive whole number or decimal')
        loan_amount_string = input()
    return loan_amount_string

def get_apr():
    prompt('What is the APR?')
    monthly_apr_string = input()
    if '%' in monthly_apr_string:
        monthly_apr_string = monthly_apr_string.replace('%','')
    while invalid_number_float(monthly_apr_string):
        prompt('APR must be 0 or greater')
        monthly_apr_string = input()
    return monthly_apr_string

def get_loan_length():
    while True:
        prompt('What is the loan length in years and months?')

        loan_length_years = input('Years: ')
        while invalid_number_int(loan_length_years):
            prompt('Please provide a positive whole number')
            loan_length_years = input('Years: ')
        loan_length_months = input('Months: ')
        while invalid_number_int(loan_length_months):
            prompt('Please provide a whole number')
            loan_length_months = input('Months: ')
        loan_length_total = ((int(loan_length_years) * MONTHS_IN_YEAR)
                            + int(loan_length_months))
        if loan_length_total == 0:
            prompt('Loan length must be at least 1 month')
        elif loan_length_total > 0:
            break

    return loan_length_total

def calc_monthly_payments():
    loan_amount_float = float(get_loan_amount())
    monthly_apr_float = float(get_apr()) / 100 # converts percentage to decimal
    annual_apr_float = monthly_apr_float / MONTHS_IN_YEAR
    loan_duration_int = get_loan_length()

    if monthly_apr_float == 0:
        monthly_payments = loan_amount_float / loan_duration_int
        return monthly_payments
    monthly_payments = (loan_amount_float * annual_apr_float
                            / (1 - (1 + annual_apr_float)
                            ** (-loan_duration_int)))
    return monthly_payments

def display_monthly_payments(output):
    prompt(f'Your monthly repayments will be: £{output:.2f}')

def get_carry_on():
    prompt('Do you want to do another calculation? (y/n)')
    carry_on = input()
    while carry_on not in ['n', 'N', 'y', 'Y']:
        prompt('Please enter y or n')
        carry_on = input()
    if carry_on in ['n', 'N']:
        return False
    if carry_on in ['y', 'Y']:
        os.system('clear')
        return True
    return None

os.system('clear')
display_welcome()
while True:
    output_monthly_payments = calc_monthly_payments()
    display_monthly_payments(output_monthly_payments)
    if not get_carry_on():
        prompt('Thank you for using the Repayment Calculator!')
        break
    