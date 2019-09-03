MSP = "---" + u'\u2510' + "\n   O\n   |\n  /|\\\n   |\n  / \\"
def main():
    x = 4
    word = input ("Player 1, what is the word? ")
    wordArr = word.split()
    #guessesused = 8
    print("\n"*50)
    guessNum = 0
    workingWord = ""
    for n in wordArr:
        workingWord += "-"*len(n)+" "
    word = word.lower()
    while (workingWord.split() != word.split() and guessNum < 8):
        print("\n"*50)
        print(MSP[:x])
        guessCorrect = False
        print((workingWord))
        guess = input("Player 2, guess a letter ").lower()
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
            elif(guessNum == 4 or guessNum == 5):
                x+=1
            elif(guessNum == 8):
                x+=2
            else:
                x += 5
    if(workingWord.split() == word.split()):
        print("Player Two wins, the word was: "+word)
    else:
        print(MSP)
        print("Player One wins, the word was: "+word)
    playAgain = input("Play Again y/n ")
    if(playAgain == "y"):
        main()
    else:
        raise SystemExit
main()


            
