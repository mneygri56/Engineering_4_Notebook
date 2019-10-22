#!/bin/bash
str="Hello World!" #declares the string
for i in {1..10} #run the loop 10 times
do
str="$str $str" #concatenates the string with itself, doubles length
echo $str #prints the final (massive) string to the terminal
done
