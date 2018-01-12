"""
Exercise 17: Blood Alcohol Calculator

Create a program that prompts for your weight, gender, number of drinks, the amount of alcohol
by volume of the drinks consumed, and amount of time since your last drink.

Calculate you blood alcohol content (BAC) using this formula:

BAC = (A * 5.14 / W * r) - .015 x H

where:
A is the total alcohol consumed in ounces(oz).
W is the body weight in pounds.
r is the alcohol distribution ratio:
 - 0.73 for men
 - 0.66 for women

H is the number of hours since the last drink.

Display whether or not it's legal to drive by comparing the blood alcohol content
to 0.08.

http://projects.madmax.io/?p=68
"""
from ex_17_bac_calc_functions import *

def bac_calculator():
    greeting()
    weight = weight_input_and_converter()
    sex_input = sex_input_and_checker()
    num_of_drinks = number_of_drinks()
    alc_per_drink = alc_content()
    hours_since_last_drink = last_drink()
    bac_computations(a=num_of_drinks, b=alc_per_drink, w=weight, s=sex_input, h=hours_since_last_drink)

bac_calculator()
