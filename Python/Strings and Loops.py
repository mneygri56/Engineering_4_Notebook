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
