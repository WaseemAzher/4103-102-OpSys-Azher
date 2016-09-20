#!/bin/bash

Myfile=$(basename "$1" | cut -d. -f1)
Curdate="_$(date +"%Y-%m-%d")"
NewName=$Myfile$Curdate
Newfile=${1/$Myfile/$NewName}
cp $1 $Newfile
