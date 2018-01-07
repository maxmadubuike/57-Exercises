'''
Exercise 23: Troubleshooting Car Issues

Create a program that walks the user through troubleshooting
issues with a car.
'''
import sys

def yes_or_no_input_checker(a, b):
    reenter_input = "Please enter 'y' for yes or 'n' for no."

    if a.isnumeric():
        print(reenter_input)
        b()
    elif a.isalpha():
        a_lower = a.lower()
        if len(a_lower) != 1:
            print(reenter_input)
            b()
        else:
            if a_lower == 'y' or a_lower == 'n':
                return a_lower
            else:
                print(reenter_input)
                b()

def greeting():
    print("Welcome to the Exercise 23: Troubleshooting Car Issues")
    print("Please enter 'y' or 'n' to the following questions.")

def first_answer():
    first_choice_uncleaned = input("Is the car silent when you turn the key?\t")

    first_choice_cleaned = yes_or_no_input_checker(a=first_choice_uncleaned, b=first_answer)
    if first_choice_cleaned == 'y':
        _1y()
    elif first_choice_cleaned == 'n':
        _1n()

def _1y():
    second_choice_uncleaned = input("Are the battery terminals corroded?\t")

    second_choice_cleaned = yes_or_no_input_checker(a=second_choice_uncleaned, b=_1y)

    if second_choice_cleaned == 'y':
        _1y_2y()
    elif second_choice_cleaned == 'n':
        _1y_2n()

def _1n():
    second_choice_uncleaned = input("Does the car make a clicking noise?\t")

    second_choice_cleaned = yes_or_no_input_checker(a=second_choice_uncleaned, b=_1n)

    if second_choice_cleaned == 'y':
        _1n_2y()
    elif second_choice_cleaned == 'n':
        _1n_2n()

def _1y_2y():
    print("Clean the terminals and try starting again.")
    sys.exit()

def _1y_2n():
    print("Replace the cables and try again.")
    sys.exit()

def _1n_2y():
    print("Replace the battery.")
    sys.exit()

def _1n_2n():
    third_answer_uncleaned = input("Does the car crank up but fail to start?\t")

    third_answer_cleaned = yes_or_no_input_checker(a=third_answer_uncleaned, b=_1n_2n)

    if third_answer_cleaned == 'y':
        _1n_2n_3y()
    elif third_answer_cleaned == 'n':
        _1n_2n_3n()

def _1n_2n_3y():
    print("Check spark plug connections.")
    sys.exit()

def _1n_2n_3n():
    fourth_answer_uncleaned = input("Does the engine start and then die?\t")

    fourth_answer_cleaned = yes_or_no_input_checker(a=fourth_answer_uncleaned,b=_1n_2n_3n)

    if fourth_answer_cleaned == 'y':
        _1n_2n_3n_4y()
    elif fourth_answer_cleaned == 'n':
        print("Get it in for service.")
        sys.exit()

def _1n_2n_3n_4y():
    fifth_answer_uncleaned = input("Does your car have fuel inejction?\t")

    fifth_answer_cleaned = yes_or_no_input_checker(a=fifth_answer_uncleaned,b=_1n_2n_3n_4y)

    if fifth_answer_cleaned == 'y':
        print("Get it in for service.")
        sys.exit()
    elif fifth_answer_cleaned == 'n':
        print("Check to ensure the choke is opening and closing.")
        sys.exit()
