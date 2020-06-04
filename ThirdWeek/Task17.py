s = str(input())
pos1 = s.find("f")
pos2 = s. find("f", pos1 + 1)
if pos1 == pos2 and pos1 != -1:
    print("-1")
elif pos1 != -1 and pos1 != pos2:
    print(pos2)
else:
    print("-2")
