import sys
d = dict()
d0 = dict()
d1 = dict()
allBalls = 0
inFile = open('input.txt')
for line in inFile:
    line = line.split()
    party = " ".join(line[0:-1])
    balls = int(line[-1])
    d.setdefault(party, 0)
    d[party] += balls
    allBalls += balls
inFile.close()
for i in d:
    d0[i] = (d[i] * 450) // allBalls
    d1[i] = (d[i] * 450) / allBalls
    d1[i] = d1[i] - d0[i]
if sum(d0.values()) < 450:
    sor = sorted(d1.items(), key=lambda x: x[1], reverse=True)
    j = sum(d0.values())
    while True:
        if j == 450:
            break
        for i in sor:
            if j == 450:
                break
            j += 1
            d0[i[0]] += 1
for i in d0:
    print(i, d0[i])
