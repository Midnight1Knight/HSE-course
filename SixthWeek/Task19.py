inFile = open('input.txt', 'r')
parties = []
for line in inFile:
    if line == 'PARTIES:\n':
        continue
    if line == 'VOTES:\n':
        break
    parties.append(line)
sortList = []
for i in range(len(parties)):
    sortList.append([parties[i], 0])
for line in inFile:
    for i in range(len(parties)):
        if line == parties[i]:
            sortList[i][1] += 1
sortList.sort(key=lambda x: (x[1] * -1, x[0]))
for i in range(len(parties)):
    print(sortList[i][0], end="")
inFile.close()
