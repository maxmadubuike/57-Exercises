from us_state_abbreviations import states
import decimal

D = decimal.Decimal

def greeting():
    print("Welcome to exercise 20: The Multistate Sales Tax Calculator.")

def alphabet_only_checker(a, b):
    if a.isnumeric():
        print("Please enter only letters.")
        b()
    elif a.isalpha():
        return a

def number_only_checker_and_dec_converter(a, b):
    try:
        a_cleaned = D(a)
        return a_cleaned
    except ValueError:
        print("Please enter a number")
        b()


def order_amount_input():
    order_amount_uncleaned = input("What is the order amount?\n")

    order_amount_cleaned = number_only_checker_and_dec_converter(a=order_amount_uncleaned,b=order_amount_input)

    return order_amount_cleaned

def state_input():
    state_uncleaned = input("What state do you live in?\nEnter state as two letter abreviation.\n"+
    "For example: 'Texas' as 'tx'.  Case does not matter.\n")

    # Validating input as alphabet only
    state_uncleaned_after_alphabet_checker = alphabet_only_checker(a=state_uncleaned,b=state_input)

    # Validating length of input
    if len(state_uncleaned_after_alphabet_checker) != 2:
        print("Please enter state as two letter abreviation.")
        state_input()
    elif len(state_uncleaned_after_alphabet_checker) == 2:
        state_uncleaned_length_confirmed = state_uncleaned_after_alphabet_checker.upper()

    # Validating 2 letter input
    if state_uncleaned_length_confirmed in states:
        state_input_clean_and_valid = state_uncleaned_length_confirmed
        return state_input_clean_and_valid
    elif state_uncleaned_length_confirmed not in states:
        print("That is not a valid 2 letter state.  Please try again.")
        state_input()

def total_calculations(order_amount, state):
    if state == 'WI':
        tax =  D(1.05)
        tax_amount_uncleaned = order_amount * D(0.05)
        tax_amount_cleaned = round(tax_amount_uncleaned, 2)
        pre_round_total = order_amount * tax
        final_total = round(pre_round_total, 2)
        print("The tax is ${}".format(tax_amount_cleaned))
        print("The total is ${}".format(final_total))



    else:
        tax =  D(1.08)
        tax_amount_uncleaned = order_amount * D(0.08)
        tax_amount_cleaned = round(tax_amount_uncleaned, 2)
        pre_round_total = order_amount * tax
        final_total = round(pre_round_total, 2)
        print("The tax is ${}".format(tax_amount_cleaned))
        print("The total is ${}".format(final_total))
