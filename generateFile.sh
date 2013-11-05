#!/bin/bash

cppTemplate=("cppClassTemplate" "hppTemplate" "cppMainTemplate" "cppTemplate" "hppClassTemplate" "makeFileTemplate")
cTemplate=("cMainTemplate" "cTemplate" "cTemplate" "makeFileTemplate")

#filename=""
extention=$1
#include=""

class_list=()
file_list=()
main=$2
file_option=false
class_option=false
for param in "$@"
do
    if [ "$param" == "-c" ]; then
        class_option=true
        file_option=false
    elif [ "$param" == "-f" ]; then
        class_option=false
        file_option=true
    elif [ "$class_option" == "true" ]; then
        class_list+=("$param")
    elif [ "$file_option" == "true" ]; then
        file_list+=("$param")
    fi
done
