'''
Exercise 19: BMI Calculator
Create a program to calculate the body mass index (BMI) for a person using the
person's height in inches and weight in pounds.  The program should prompt
the user for weight and height.

Calculate the BMI by usingthe following formula:

bmi = (weight / (height * height)) * 703

If the BMI is between 18.5 and 25, display that the person is at a normal weight.
If they are out of that range, tell them if they are underweight or overweight
and tell them to consult their doctor.
'''

from ex_19_bmi_calculator_func import *

def bmi_calculator():
    greeting()
    height = height_input()
    weight = weight_input()
    bmi = calculations(height=height, weight=weight)
    result(bmi)

bmi_calculator()
