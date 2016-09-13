#!/bin/bash

inputs=$@
sum=0

for num in $inputs
 do
   ((sum+=num))
 done

echo $sum
