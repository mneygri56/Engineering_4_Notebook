#!bin/bash

# this script makes 2 leds blink 10 times each

gpio mode 0 out #sets up gpio pin
gpio mode 1 out #sets up gpio pin


for i in {1..10} #runs the loop 10 times
do
gpio write 0 1 #turns led on
gpio write 1 1 #turns other led on
sleep 0.5 #wait for half a second
gpio write 0 0 #turns led off
gpio write 1 0 #turns other led off
sleep 0.5 #wait for half a second
done
