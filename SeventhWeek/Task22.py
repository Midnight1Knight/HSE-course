from collections import defaultdict
history = defaultdict(lambda: defaultdict(int))
with open('input.txt') as inFile:
    for line in inFile:
        person, thing, val = line.split()
        history[person][thing] += int(val)
for person in sorted(history):
    print(person, ':', sep="")
    for thing in sorted(history[person]):
        print(thing, history[person][thing])
