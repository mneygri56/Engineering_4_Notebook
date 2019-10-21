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
