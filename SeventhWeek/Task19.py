with open('input.txt') as inFile:
    words = inFile.read().split()
d = dict()
for word in words:
    d.setdefault(word, 0)
    d[word] += 1
for word in sorted(d.items(), key=lambda x: (-x[1], x[0])):
    print(word[0])
