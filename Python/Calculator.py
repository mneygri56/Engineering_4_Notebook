#Calculator
#Written By David and Miles

print("x to exit")

def doMath(first, second, operation): #function to do math
    num = 0 #variable to be output
    if(operation == 1): #addition
        num = first+second 
    if(operation == 2): #subtraction
        num = first-second
    if(operation == 3): #multiplication
        num = first*second
    if(operation == 4): #division, rounded to two decimals
        num = round(first/second, 2)
    if(operation == 5): #modulus
        num = int(first)%int(second)
    return num
while(True):
    numOne = input("First Number") 
    numTwo = input("Second Number")
    if(numOne == 'x' or numTwo == 'x'):#exit condition
        raise SystemExit
    #calls to doMath to get outputs
    print("Sum:\t\t" + str(doMath(float(numOne), float(numTwo), 1)))
    print("Difference:\t" + str(doMath(float(numOne), float(numTwo), 2)))
    print("Product:\t" + str(doMath(float(numOne), float(numTwo), 3))) 
    print("Quotient:\t" + str(doMath(float(numOne), float(numTwo), 4)))
    print("Modulo:\t\t" + str(doMath(float(numOne), float(numTwo), 5)))
