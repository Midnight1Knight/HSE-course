inFile = open('input.txt', 'r')
parties = []
for line in inFile:
    if line == 'PARTIES:\n':
        continue
    if line == 'VOTES:\n':
        break
    parties.append(line)
votes = [0] * len(parties)
for line in inFile:
    for i in range(len(parties)):
        if parties[i] == line:
            votes[i] += 1
sumOfVotes = sum(votes)
for i in range(len(votes)):
    if votes[i] / sumOfVotes * 100 >= 7:
        print(parties[i], end='')

inFile.close()
