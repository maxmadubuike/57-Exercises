"""
Sometimes you have to perform a more complex calculation based on some provided inputs and
then use that result to make a determination.

Create a program that prompts for your weight, gender, number od firnks, the amount of alcohol
by volume of the drinks consumed, and amount of time since your last drink.

Calculate you blood alcohol content (BAC) using this formula:

BAC = (A X 5.14/W XR) - .015 x H

where:
A is the total alcohol consumed in ounces(oz).
W is the body weight in pounds.
r is the alcohol distribution ratio:
 - 0.73 for men
 - 0.66 for women

H is the number of hours since the last drink.

Display whether or not it's legal to drive by comparing the blood alcohol content
to 0.08.
"""
import sys

def greeting():
    print("Welcome to the Blood Alcohol Checker!")
    print("Please use responsibly")
    print("To quit at anytime, type 'q' or 'quit'")
    print("Let's begin.\n")

def quit_checker(a):
    if a == 'q' or a == 'quit':
        print("Thank you for using BAC Calculator.")
        sys.exit()
    else:
        return a

# Weight
def weight_input_and_converter():
    raw_weight = input("Please enter your weight in pounds.\n")
    quit_checker(raw_weight)
    if raw_weight.isnumeric():
        int_weight = int(raw_weight)
        return int_weight
    else:
        print("This is not a number.")
        weight_input_and_converter()

# Sex
def sex_input_and_checker():
    sex_input_unchecked = input("Are you male or female?\nEnter 'm' for male or 'f' for female.\n")

    quit_checker(sex_input_unchecked)

    if sex_input_unchecked.lower() == ('m'):
        sex_input_cleaned = sex_input_unchecked.lower()
        return sex_input_cleaned
    elif sex_input_unchecked.lower() == ('f'):
        sex_input_cleaned = sex_input_unchecked.lower()
        return sex_input_cleaned
    else:
        print("Incorrect input. Please enter 'm' for male, or 'f' for female.")
        sex_input_and_checker()

# Number of Drinks
def number_of_drinks():
    numb_of_drinks = input("How many drinks have you consumed?  Enter a whole number.\n")

    quit_checker(numb_of_drinks)

    if numb_of_drinks.isnumeric():
        int_numb_of_drinks = int(numb_of_drinks)
        if int_numb_of_drinks < 1:
            print("You haven't had any drinks.  Your BAC is zero.")
            sys.exit()
    return int_numb_of_drinks

# Alcohol Content
def alc_content():
    print("For the following section enter percents as whole numbers.")
    print("For example: 33'%'' would be entered as '33'")
    content_by_volume_uncleaned = input("What was the average alcoholic content of the drinks?\n")

    quit_checker(content_by_volume_uncleaned)

    if content_by_volume_uncleaned.isnumeric():
        content_by_volume_clean = int(content_by_volume_uncleaned) / 100
        return content_by_volume_clean
    else:
        print("Please enter a number!")
        alc_content()

def last_drink():
    print("The next section deals with your last drink.")
    print("For times less than an hour, enter 0'.")
    hours_since_last_drink_uncleaned = input("How many hours ago did you have your last drink?\n")

    quit_checker(hours_since_last_drink_uncleaned)

    if hours_since_last_drink_uncleaned.isnumeric():
        int_hours = int(hours_since_last_drink_uncleaned)
        return int_hours
    else:
        print("Please enter a number.")
        last_drink()

def bac_computations(a, b, w, s, h):

    # p1 = A * 5.14 in the forumla, where A = total drinks * ounces per drink
    total_ounces = a * b
    p1 = total_ounces * 5.14

    # p2 = W * r in the forumla

    if s == 'm':
        p2 = w * 0.73
    else:
        p2 = w * 0.66

    p3 = 0.015 * h

    first_operation = p1 / p2
    second_operation = first_operation - p3

    if second_operation > 0.08:
        print("Your BAC is {}.".format(second_operation))
        print("It is not legal for you to drive.")
    elif second_operation <= 0.08:
        print("Your BAC is {}.".format(second_operation))
        print("It is legal for you to drive.  Be careful.")
    return second_operation
