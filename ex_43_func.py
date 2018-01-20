import os

def greeting():
    print("Welcome to Exercise 43: Website Generator")

def siteName():
    sitename = input("Site name: ")
    return sitename

def authorName():
    authorname = input("Author: ")
    return authorname

def javaFolder():
    javaFol = input("Do you want a folder for JavaScript?  Enter 'y' or 'n'")
    return javaFol.lower()

def cssFolder():
    cssFol = input("Do you want a folder for JavaScript?  Enter 'y' or 'n'")
    return cssFol.lower()

def siteDirectoryCreator(sitename, java, css):
    try:
        os.mkdir(sitename)
        print("Created ./{}".format(sitename))
    except OSError:
        print("/{} already exists".format(sitename))
    if os.path.exists(sitename):
        if java == 'y' and css =='y':

            os.mkdir(sitename + '/js')
            print("Created /{}/js".format(sitename))

            os.mkdir(sitename + '/css')
            print("Created /{}/css".format(sitename))

        elif java =='y' and css =='n':
            os.mkdir(sitename+ '/js')
        elif java =='n' and css =='y':
            os.mkdir(sitename + '/css')
        else:
            pass
    else:
        os.mkdir(sitename)

def siteFileCreator(sitename, author):
    os.chdir(sitename)
    file = open('index.html', 'w')
    file.write('<!DOCTYPE html>\n')
    file.write("<html>\n")
    file.write("\t<head>\n")
    file.write("\t\t<meta charset=")
    file.write("'utf-8'>\n")
    file.write("\t\t<title>{}</title>\n".format(sitename))
    file.write("\t</head>\n")
    file.write("\t<body>\n")
    file.write("\n")
    file.write("\t</body>\n")
    file.write("</html>")

    file.close()
