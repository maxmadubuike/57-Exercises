'''
Exercise 24: Anagram Checker

Create a program that compares two strings and determines if the two strings are
anagrams.  The program should prompt for both input strings and display the output
as shown in the example that follows.

Constraints:
Implement the program using a function called 'isAnagram', which takes two words as
its arguments and returns true or false.  Invoke this function from your main
program.

Check that both words are the same length

'''

from ex_24_func import *

def main():
    greeting()
    first_word = first_word_input()
    second_word = second_word_input()
    result = isAnagram(a=first_word,b=second_word,c=main)
    if result == True:
        print("{} and {} are anagrams.".format(first_word, second_word))
    elif result == False:
        print("{} and {} are not anagrams.".format(first_word, second_word))

main()
