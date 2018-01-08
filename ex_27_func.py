def greeting():
    print("Welcome to Exercise 27: Validating Inputs")

def first_name_input():
    first_name_raw = input("Enter the first name: ")
    return first_name_raw

def last_name_input():
    last_name_raw = input("Enter the last name: ")
    return last_name_raw

def fn_v(name):
    if name.isalpha() and len(name) >= 2:
        print("First Name is valid")
        return name
    elif name.isalpha():
        print("First Name must be at least 2 characters")
    else:
        print("First name must be only letters.")


def ln_v(name):
    if name.isalpha() and len(name) >= 2:
        print("Last Name is valid")
        return name
    elif name.isalpha():
        print("Last name must be at least 2 characters.")
    else:
        print("Last name must be only letters.")

def zip_code_input():
    zip_code_raw = input("Enter the ZIP code: ")
    return zip_code_raw

def zc_v(zipcode):
    if len(zipcode) != 5:
        print("Zip codes must be 5 digits long.")
    else:
        if zipcode.isnumeric():
            print("Zip code is valid.")
            return zipcode
        elif zipcode.isalnum():
            print("Zip codes must only contain numbers.")

def employeeID_input():
    empIDraw = input("Enter an employee ID: ")
    return empIDraw

def empID_type_v(employeeID):
    score = 0
    if  len(employeeID) != 7:
        score += 0

    if employeeID[0:1].isalpha():
        score += 10
    else:
        score += 0

    if employeeID[2] == '-':
        score += 10
    else:
        score += 0

    if employeeID[3:].isnumeric():
        score += 10
    else:
        score += 0

    return score

def empID_v(score):
    if score == 30:
        print("Employee ID is valid.")
    else:
        print("Employee ID is not valid.")

def validateInput(fn, ln, zc, eid):
    fn_v(fn)
    ln_v(ln)
    zc_v(zc)
    score = empID_type_v(eid)
    empID_v(score)
