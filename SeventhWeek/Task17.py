d = {}
with open('input.txt') as inFile:
    for line in inFile:
        c, v = line.strip().split()
        d.setdefault(c, 0)
        d[c] += int(v)
for i in sorted(d.items()):
    print(*i)
