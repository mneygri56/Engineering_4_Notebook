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
  
```python
  
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

### Calculator
The goal of this assignment was to create a program with a function that could calculate the sum, difference, quotient, and product of two inputs

#### Code

<details>
  <summary> This man can calculate large sums in his head, #3 will suprise you (Not Clickbait)</summary>
  
  ```python
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
    
  ```
  
</details>

### Quadratic Solver

Ever been in math class and wanted an easy way to calculate those weird quadratics, well you've got it.

#### Code
This program prints out the roots of a quadratic given the coefficients, call now and we'll double your order, just call 1-800-not-scam

<details>
  <summary>Act fast, our first 30 customers get a free code with their order</summary>
  
  ```python
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
        
  ```
 
 </details>
 
 ### Hello Git
This project was setting up github on the pi. Github has sinced ceased to function for no reason, so we decided to make our own github:

1st, put the changed files onto a flash drive (The "hub")

2nd, download them onto another computer (The "Git")

3rd, Commit and Push

Yay hubGit™!!!

### Git Forks and Clones
We forked a repository called class accounts, and cloned it to the pi, added our names to it, then committed it.

We want to make sure we pull recent changes from github before pushing

## Awesome Python Code Part thats really fun stuff

### Strings and Loops
This program was a little tricky, we had to learn how to split strings, so that's my lessons learned, the split() function is really useful.

<details>
  <summary>Code</summary>
  ```python
    
	#Strings and Loops
	#Written By David and Miles
	while(True):
		#Get a User Input
	    sentence = input("Enter a Sentence: ")
	    #Split the Input by Spaces
	    splitsentence = sentence.split()

	    for n in range(len(splitsentence)):
		#if the sentence is over, end the system
		if (splitsentence[n] == "-1"):
			raise SystemExit
		#Otherwise, print out each character in the string
		for x in range(len(splitsentence[n])):
		    print(splitsentence[n][x])
		#print a - between words
		print("-")
     ```
  
  </details>
  
### Man Shaped Pinata (Pronounced Pin-ate-ae, no accent whatsoever)
This program was to make a "Man Shaped Pinata" game, which is basically (whispers) Hangman (/whispers) This was a bit frustrating, the first program with a "Problems" Section!

#### Code
<details>
  <summary>Code</summary>
  ```python
	#Man Shaped Pinata word guessing game
	#Written by David and Miles
	import getpass
	#Define how one makes the man shaped pinata
	MSP = "---" + u'\u2510' + "\n   O\n   |\n  /|\\\n   |\n  / \\"
	def main():
	    #x is the number of characters in the man shaped pinata to print
	    x = 4

	    #get the word
	    word = getpass.getpass("Player 1, what is the word? ")
	    wordArr = word.split()
	    guessList = []
	    #Clear the terminal
	    print("\n"*50)
	    guessNum = 0
	    workingWord = ""
	    spacesAfter = 0
	    #get the "working word" which is how much player two has guessed
	    for n in wordArr:
		workingWord += "-"*len(n)+" "
	    #put the word into lowercase
	    word = word.lower()
	    #while guesses is less than 8 and the words havent been guessed
	    while (workingWord.split() != word.split() and guessNum < 8):
		#clear screen, print out the Man shaped pinata, print the amount that
		#has been guessed followed by the letters that have been guessed
		print("\n"*50)
		print(MSP[:x]+"\n"*(5-spacesAfter))
		guessCorrect = False
		print((workingWord))
		print("Previously guessed: " + ", ".join(guessList))
		guess = raw_input("Player 2, guess a letter ").lower()
		isUsed = True
		while(isUsed):
		    isUsed = False
		    #if n has already been guessed, give them another shot
		    for n in guessList:
			if(n == guess):
			    isUsed = True
		    if(not isUsed):
			guessList.append(guess)
		    else:
			print("Already Guessed FOOL")
			guess = raw_input("Player 2, guess a letter AGAIN ").lower()
		#if the letter is in the word, change working word to have that letter
		#in the right place, otherwise ...
		for n in range(len(workingWord)-1):
		    if (guess == word[n]):
			workingList = list(workingWord)
			workingList[n] = guess
			workingWord = "".join(workingList)
			guessCorrect = True
		if(guess.split() == word.split()):
		    workingWord = word
		    guessCorrect = True
		#... Otherwise add to x so that the next piece is revealed
		if (guessCorrect == False):
		    guessNum+=1
		    if(guessNum == 7 or guessNum == 3):
			x+=4
			spacesAfter +=1
		    elif(guessNum == 4 or guessNum == 5):
			x+=1
		    elif(guessNum == 8):
			x+=2
		    else:
			spacesAfter +=1
			x += 5
	    #Win conditions, the word has been guessed, player two wins
	    #too many guesses, player one wins
	    if(workingWord.split() == word.split()):
		print("Player Two wins, the word was: "+word)
	    else:
		print(MSP)
		print("Player One wins, the word was: "+word)
	    #see if they want to play again
	    playAgain = raw_input("Play Again y/n ")
	    if(playAgain == "y"):
		main()
	    else:
		raise SystemExit
	main()
       ```
  
  </details>
