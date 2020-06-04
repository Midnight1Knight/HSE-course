d = dict()
inFile = open('input.txt', 'r', encoding='utf-8')
outFile = open('output.txt', 'w', encoding='utf-8')
for i in inFile:
    d.setdefault(i, 0)
    d[i] += 1
inFile.close()
cand = sorted(d.items(), key=lambda x: x[1], reverse=True)
if max(d.values()) / sum(d.values()) > 0.5:
    outFile.write(cand[0][0])
else:
    outFile.write(cand[0][0])
    outFile.write(cand[1][0])
outFile.close()
