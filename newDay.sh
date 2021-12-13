#!/bin/bash
# Make a new folder named day##  with the number specified
# Copy the code template into that folder and start editing
day=$1
foldername="day"$day;
mkdir $foldername;
cp template.py $foldername"/code.py";
cd $foldername;
nvim "test.txt" "code.py";

