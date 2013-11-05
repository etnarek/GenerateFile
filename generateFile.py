#!/bin/python3
import sys

def fileMaker(template, replaceList, fileName):
    infile = open(template)
    outfile = open(fileName, 'w')
    for line in infile:
        for src, target in replaceList:
            line = line.replace(src, target)
        outfile.write(line)
    infile.close()
    outfile.close()

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
    replace=[]
    includes=""
    sources=""
    head_extension=""
    template={}
    if extension == "cpp":
        template=cppTemplate
        head_extension="hpp"
        for inc in classList:
            includes+="#include "+inc+".hpp\n"
            sources+=inc+".cpp "
    elif extension == "c":
        template=cTemplate
        head_extension="h"

    for fyle in fileList:
        includes+="#include "+fyle+"."+head_extension+"\n"
        sources+=fyle+"."+extension+" "

    sources+=mainFile+"."+extension

    #main
    replace=[("@include", includes)]
    fileMaker(template["main"], replace, mainFile+"."+extension)

    #MakeFile
    replace=[("@sources", sources), ("@extension", extension), ("@executable", mainFile)]
    fileMaker(template["make"], replace, "makefile")

    #for it in replace:
    #    print(it)



# (Template, ReplaceList, FileName)

if __name__=='__main__':
    main()
