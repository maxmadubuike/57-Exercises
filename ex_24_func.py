def greeting():
    print("Welcome to Exercise 24: Anagram Checker!")
    print("Enter two strings and I'll tell you if they are anagrams.")

def first_word_input():
    first_word_unclean = input("Enter the first string:\t")

    if first_word_unclean.isnumeric():
        print("Please enter a word. No numbers.")
        return first_word_input()
    elif first_word_unclean.isalpha():
        first_word_clean = first_word_unclean.lower()
        return first_word_clean

def second_word_input():
    second_word_unclean = input("Enter the second string: ")

    if second_word_unclean.isnumeric():
        print("Please enter a word. No numbers.")
        return second_word_input()
    elif second_word_unclean.isalpha():
        second_word_clean = second_word_unclean.lower()
        return second_word_clean

def isAnagram(a,b,c):
    anagram_valid = ''
    if len(a) != len(b):
        print("The words must be the same length in order to be an anagram.")
        print("Please try again.")
        c()
    else:
        for letter in a:
            if letter in b:
                return True
            else:
                return False
