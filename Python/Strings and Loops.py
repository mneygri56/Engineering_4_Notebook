
while(True):
    sentence = input("Enter a Sentence: ")
    splitsentence = sentence.split()

    for n in range(len(splitsentence)):
        if (splitsentence[n] == "-1"):
                raise SystemExit
        for x in range(len(splitsentence[n])):
            print(splitsentence[n][x])
        print("-")
