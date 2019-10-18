print("x to exit")

def doMath(first, second, operation):
    num = 0
    if(operation == 1):
        num = first+second
    if(operation == 2):
        num = first-second
    if(operation == 3):
        num = first*second
    if(operation == 4):
        num = round(first/second, 2)
    if(operation == 5):
        num = int(first)%int(second)
    return num
while(True):
    numOne = input("First Number")
    numTwo = input("Second Number")
    if(numOne == 'x' or numTwo == 'x'):
        raise SystemExit
    print("Sum:\t\t" + str(doMath(float(numOne), float(numTwo), 1)))
    print("Difference:\t" + str(doMath(float(numOne), float(numTwo), 2)))
    print("Product:\t" + str(doMath(float(numOne), float(numTwo), 3)))
    print("Quotient:\t" + str(doMath(float(numOne), float(numTwo), 4)))
    print("Modulo:\t\t" + str(doMath(float(numOne), float(numTwo), 5)))
