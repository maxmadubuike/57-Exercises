import requests

def greeting():
    print("Welcome to Exercise 47: Who's in Space!")
    print("\n")

def getInfoFromAPI():
    r = requests.get('http://api.open-notify.org/astros.json')
    info = r.json()
    infoDict = dict(info)
    return infoDict

def infoProcessing(apiinfo):
    print("There are {} people in space right now.".format(apiinfo['number']))
    print("\n")
    people = apiinfo['people']

    ######## Table Length ########
    tabLen = 0
    maxNameLen = 0
    maxCraftLen = 0

    ######## Table Parts########
    spaces = " "
    tableColumn1 = "Name"
    nameSpaces = 2

    tableColumn2 = "Craft"
    craftSpaces = 2

    tableLine = "|"
    columBorder = "-"

    ######## Defining maximum table length values ########

    for dic in people:
        a = dic['name']
        b = dic['craft']

        if len(a) + len(b) > tabLen:
            tabLen = len(a) + len(b) + nameSpaces + craftSpaces + len(tableLine)
        if len(a) + nameSpaces > maxNameLen:
            maxNameLen = len(a) + nameSpaces
        if len(b) + craftSpaces > maxCraftLen:
            maxCraftLen = len(b) + craftSpaces

    ######## Building the table headers ########

    print(tableColumn1, end='')
    print(spaces*(maxNameLen-(len(tableColumn1))), end='')
    print(tableLine, end='')
    print(spaces*craftSpaces, end='')
    print(tableColumn2)
    print(columBorder*(tabLen + maxCraftLen - len(tableLine)- craftSpaces))

    ######## Populating the table ########

    for dic in people:
        a = dic['name']
        b = dic['craft']
        print(a, end='')
        print(spaces*(maxNameLen-len(a)), end='')
        print(tableLine, end='')
        print(spaces*craftSpaces, end='')
        print(b)
