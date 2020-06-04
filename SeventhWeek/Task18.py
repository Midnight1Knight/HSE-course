from collections import OrderedDict
with open('input.txt') as inFile:
    lines = inFile.read().split()
dict_ = dict()
for i in range(len(lines)):
    dict_.setdefault(lines[i], 0)
    dict_[lines[i]] += 1
print(sorted(dict_.items(), key=lambda x: (-x[1], x[0]))[0][0])
