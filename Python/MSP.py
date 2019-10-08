import getpass
MSP = "---" + u'\u2510' + "\n   O\n   |\n  /|\\\n   |\n  / \\"
def main():
    x = 4
    word = getpass.getpass("Player 1, what is the word? ")
    wordArr = word.split()
    guessList = []
    print("\n"*50)
    guessNum = 0
    workingWord = ""
    spacesAfter = 0
    for n in wordArr:
        workingWord += "-"*len(n)+" "
    word = word.lower()
    while (workingWord.split() != word.split() and guessNum < 8):
        print("\n"*50)
        print(MSP[:x]+"\n"*(5-spacesAfter))
        guessCorrect = False
        print((workingWord))
        print("Previously guessed: " + ", ".join(guessList))
        guess = raw_input("Player 2, guess a letter ").lower()
        isUsed = True
        while(isUsed):
            isUsed = False
            for n in guessList:
                if(n == guess):
                    isUsed = True
            if(not isUsed):
                guessList.append(guess)
            else:
                print("Already Guessed FOOL")
                guess = raw_input("Player 2, guess a letter AGAIN ").lower()
        for n in range(len(workingWord)-1):
            if (guess == word[n]):
                workingList = list(workingWord)
                workingList[n] = guess
                workingWord = "".join(workingList)
                guessCorrect = True
        if(guess.split() == word.split()):
            workingWord = word
            guessCorrect = True
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
    if(workingWord.split() == word.split()):
        print("Player Two wins, the word was: "+word)
    else:
        print(MSP)
        print("Player One wins, the word was: "+word)
    playAgain = raw_input("Play Again y/n ")
    if(playAgain == "y"):
        main()
    else:
        raise SystemExit
main()
