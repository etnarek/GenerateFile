#!/bin/python3
import sys

def main():
    path="/etc/g--/"
    cppTemplate={"main":"cppMainTemplate","make":"makeFileTemplate", "class":["cppClassTemplate", "hppClassTemplate"], "file":["cppTemplate", "hppTemplate"]}
    cTemplate={"main":"cMainTemplate","make":"makeFileTemplate", "file":["cTemplate", "hTemplate"]}

    args=sys.argv
    extension=args[1]
    mainFile=args[2]

    classOption=False
    fileOption=False
    classList=[]
    fileList=[]

    for param in args:
        if param == "-c":
            classOption=True
            fileOption=False
        elif param == "-f":
            classOption=False
            fileOption=True
        elif classOption:
            classList.append(param)
        elif fileOption:
            fileList.append(param)


if __name__=='__main__':
    main()
