inFile = open('input.txt')
setOfWords = dict()
lst = inFile.read().split()
for word in lst:
    if word not in setOfWords:
        setOfWords[word] = 0
    else:
        setOfWords[word] += 1
    print(setOfWords[word], end=" ")
inFile.close()
