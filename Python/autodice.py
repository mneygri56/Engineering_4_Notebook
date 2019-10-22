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
