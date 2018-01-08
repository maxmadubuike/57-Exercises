import re
import sys

def greeting():
    print("Welcome to Exercise 25: Password Strength Indicator")

def password_input():
    password_raw = input("Please enter your password for evaluation:  ")
    return password_raw

def passwordValidator(password):
    score = 0
    special_characters = "!@#$%^&"

    if password.isnumeric() and len(password) < 8:
        score += 25
        return score
    elif password.isalpha() and len(password) < 8:
        score += 30
        return score
    elif password.isalnum and len(password) < 8:
        score += 50
        return score
    elif password.isalnum and len(password) >= 8:
        score += 75
        for letter in password:
            if letter in special_characters:
                score = 100
        return score



def passwordResults(orig_pass, score):
    if score <= 25:
        print("The password '{}' is a very weak password.".format(orig_pass))
    elif score >= 26 and score <= 50:
        print("The password '{}' is a weak password.".format(orig_pass))
    elif score >= 51 and score <= 75:
        print("The password '{}' is a strong password.".format(orig_pass))
    elif score >= 76 and score <= 100:
        print("The password '{}' is a very strong password.".format(orig_pass))
    sys.exit()
