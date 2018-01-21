'''
Exercise 47: Who's in Space?

Visit http://api.open-notify.org/astros.json to see not only how many people
are currently in space, but also their names and which spacecraft they are on.

Create a program that pulls in data and displays the information in a tabular
format.
'''
from ex_47_func import *

def main():
    greeting()
    info = getInfoFromAPI()
    infoProcessing(apiinfo=info)

main()
