#!/bin/bash

Myfile=$1

date="$(date +%F)_"
 echo $date

Newfile=$date$Myfile
 echo $Newfile
cp $Myfile $Newfile
