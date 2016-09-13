#!/bin/bash

Myfile=$1

date="$(date +%F)_"
# echo $Curdate

Newfile=$date$Myfile
# echo $Newfile
cp $Myfile $Newfile
