#!/bin/bash
count=1
for i in "$@"
do 
echo "parametr $count = $i"
count=$(($count+1))
done