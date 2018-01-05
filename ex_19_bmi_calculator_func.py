def greeting():
    print("Welcome to Exercise 19: BMI Calculator!")
    print("Please enter only numeric values as prompted.")

def height_input():
    height = input("What is your height in inches?\n")
    if height.isnumeric():
        int_height = int(height)
        return int_height
    elif height.isalpha():
        print("Please enter a number.")
        height_input()

def weight_input():
    weight = input("What is your weight in pounds?\n")
    if weight.isalpha():
        print("Please enter a number.")
        weight_input()
    elif weight.isnumeric():
        int_weight = int(weight)
        return int_weight

def calculations(height, weight):
    # p1 = height * height_input
    # p2 = weight / p1
    # p3 = p2 * 703

    p1 = height * height
    p2 = weight / p1
    p3 = p2 * 703

    return p3

def result(bmi):
    print("Your BMI is {}.".format(bmi))

    if bmi > 18.5 and bmi < 25:
        print("You are within the ideal weight range.")
    elif bmi < 18.5:
        print("You are underweight.  You should see your doctor.")
    elif bmi > 25:
        print("You are overweight. You should see your doctor.")
