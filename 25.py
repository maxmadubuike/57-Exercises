'''
Exercise 25:  Password Strength Indicator

Create a program that determines the comlexity of a given password based on these
rules:
    - A very weak password contains only numbers and is fewer than eight characters
    - A weak password contains only letters and is fewer than eight characters.
    - A strong password contains letters and at least one number and is at least
        eight characters.
    - A very strong password contains letters, numbers, and special characters
        and is at least eight characters.

Constraints:
    - Create a passwordValidator function that takes in the password as its
        argument and returns a value you can evaluate to determine the password
        strength.  Do not have the function return a string - you may need to
        support multiple languages in the future.
    - Use a single output statement.

'''

from ex_25_func import *

def main():
    greeting()
    password = password_input()
    password_score = passwordValidator(password)
    passwordResults(orig_pass=password, score=password_score)
    
main()
