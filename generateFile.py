#!/bin/python3
import sys

def main():
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
    templates=""
    replace=[]
    includes=""
    sources=""
    head_extension=""    
    if extension == "cpp":
        templates=cppTemplate
        head_extension="hpp"
        for inc in classList:
            includes+="#include "+inc+".hpp\n"
            sources+=inc+".cpp "
    elif extension == "c":
        templates=cTemplate
        head_extension="h"
    

    for fyle in fileList:
        includes+="#include "+fyle+"."+head_extension+"\n"
        sources+=fyle+"."+extension+" "

    sources+=mainFile+"."+extension 
    
    replace.append(("@include", includes))
    

    #for it in replace:
    #    print(it)

    

# (Template, ReplaceList, FileName)
main()
