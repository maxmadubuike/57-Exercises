'''
Create a program that generates a website skeleton with the following
specifications:
    - Prompt for the name of the site.
    - Prompt for the author of the site.
    - Ask if the user wants a folder for JavaScript files
    - Ask if the user wants a folder for CSS files
    - Generate an index.html file that contains the name of the site inside the
        <title> tags and the author in a <meta> tag.
'''

from ex_43_func import *

def main():
    greeting()
    nameOfSite = siteName()
    authorofSite = authorName()
    javascriptFolder = javaFolder()
    cssFolderValidator = cssFolder()
    siteDirectoryCreator(sitename=nameOfSite, java=javascriptFolder, css=cssFolderValidator)
    siteFileCreator(sitename=nameOfSite, author=authorofSite)

main()
