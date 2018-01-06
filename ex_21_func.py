"""
Exercise 21: Numbers to Names

Write a program that converts a number from 1 to 12 to the corresponding month.
Prompt for a number and display the corresponding calendar month, with 1 being
January and 12 being December.  For any value outside the range, display an
appropriate error message.

"""
months = {1: 'January',
          2: 'February',
          3: 'March',
          4: 'April',
          5: 'May',
          6: 'June',
          7: 'July',
          8: 'August',
          9: 'September',
          10: 'October',
          11: 'November',
          12: 'December'}

def greeting():
    print("Welcome to Exercise 21: Numbers to Names")

def entered_number():
    number = input("Please enter the two digit number of the month:\t")

    # Clean and validate the input
    if number.isalpha():
        print("Only enter a number.")
        entered_number()
    elif number.isnumeric():
        if len(number) > 2:
            print("Enter a number 1-12.")
            entered_number()
        else:
            return int(number)

def match(a):
    month_match = months[a]
    return month_match

def output(a):
    print("The name of the month is {}.".format(a))
