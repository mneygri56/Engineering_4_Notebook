#Automatic Dice Roller
#Written by David and Miles

import random

print("Automatic Dice Roller")
print("Enter to Roll, x to exit")
while(True):
    x = input("Roll the Dice")
    if(x == ""):
        print(random.randint(1,6))
    elif(x == "x"):
        print("Done already?")
        raise SystemExit
