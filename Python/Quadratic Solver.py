#Quadratic Solver
#Written by David and Miles
import math
print("x to exit")
print("Quadratic Solver,  \nEnter coefficients for ax^2 + bx + c = 0")

#Calculate the roots of the function given coefficients

def rootCalc(fna, fnb, fnc):
    #Calculate the Discriminant
    fnD = fnb**2 - 4*fna*fnc
    #if its more than 0, calculate two roots
    if(fnD>0):
        fnD = math.sqrt(fnD)
        roots = [round(-(b+fnD)/(2*a), 3), round((-b+fnD)/(2*a), 3)]
    #if the Discriminant is zero, calculate one root
    elif(fnD == 0):
        fnD = math.sqrt(fnD)
        roots = [round(-b/(2*a), 3)]
    #otherwise, it has no real roots
    else:
        roots = ["No Real Roots"]
    return roots
while(True):
    #ask for a, b, and c inputs
    a = input("Input a for ax^2 ")
    b = input("Input b for bx ")
    c = input("Input c for c ")
    #if a coefficient is entered as x,
    #end the program, otherwise calculate the roots
    if(a!="x" and b!="x" and c!="x"):
        a = float(a)
        b = float(b)
        c = float(c)
        newRoots = rootCalc(float(a), float(b), float(c))
        #print out all elements in the newRoots array
        print("Roots: "+str(newRoots[0:]))
    else:
        raise SystemExit
        


