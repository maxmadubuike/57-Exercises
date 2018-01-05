def greeting():
    print("Welcome to Exercise 18: Temperature Converter.")

def selection_input():
    choice = input("Press 'C' to convert from Fahrenheit to Celcius. \n" +
    "Press 'F' to convert from Fahrenheit to Celsius\n")
    if choice.isalpha():
        choice_clean = choice.lower()
        if choice_clean == 'c' or 'f':
            return choice_clean
        else:
            selection_input()
    else:
        print("Please try again.")
        selection_input()


def fah_to_cel():
    temp_uncleaned = input("Please enter the temperature in Fahrenheit: ")
    if temp_uncleaned.isnumeric():
        temp_clean = int(temp_uncleaned)
    else:
        print("Please enter only numbers.")
        fah_to_cel()

    # Math for conversion
    conversion = (temp_clean - 32) * 5 / 9
    print("The temperature in Celcius is {}.".format(conversion))
    return conversion

def cel_to_fah():
    temp_uncleaned = input("Please enter the temperature in Celcius: ")
    if temp_uncleaned.isnumeric():
        temp_clean = int(temp_uncleaned)
    else:
        print("Please enter only numbers.")
        cel_to_fah()

    # Math for conversion
    conversion = (temp_clean * 9 / 5) + 32
    print("The temperature in Fahrenheit is {}.".format(conversion))
    return conversion
