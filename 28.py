'''
Write a program that prompts the user for five numbers and computes the total
of the numbers.

Constraints
    - The program must use repetition, usch as a counted loop, not three
        separate prompts.

'''

def main():
    counter = 0
    total = 0
    while counter < 5:
        inputraw = input("Enter a number: ")
        if inputraw.isnumeric():
            num = int(inputraw)
            total += num
            counter += 1
    print("The total is {}.".format(total))

main()
