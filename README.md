# This is our Engineering 4 Notebook
Table of Contents:

## Introduction Assignments
### Hello Raspberry Pi Zero
This assigment was an introduction to bash scripts and pi stuff in general
#### Code
Our code here wasn't too complicated, so we spiced it up a bit, see for yourself;
<details>
  <summary>Code</summary>
```
#!/bin/bash
str="Hello World!" #declares the string
for i in {1..10} #run the loop 10 times
do
str="$str $str" #concatenates the string with itself, doubles length
echo $str #prints the final (massive) string to the terminal
done
```

</details>

### Hello Mathematica
Here we had to figure out how to write a line of Mathematica to make a plot with sliders

We couldn't retrieve the actual line of code that we used, but we had to use the Manipulate() function with the graph that we wanted to create two sliders that controlled constants in the equation\

### Hello Python
This boi is a die roller written in Python, we wrote a program to roll a die and print out a random number between 1 and 6

#### Code

<details>
  <summary>How to Roll a Die in Python (Ten Steps) (With Pictures!)</summary>
  
```
  
#Automatic Dice Roller
#Written by David and Miles

import random

print("Automatic Dice Roller")
print("Enter to Roll, x to exit")
while(True): #loop that runs forever
    x = input("Roll the Dice")
    if(x == ""):
        print(random.randint(1,6)) #generates random int 1-6
    elif(x == "x"): #conditional to kill program
        print("Done already?")
        raise SystemExit
```

</details>
