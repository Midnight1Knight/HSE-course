def drugie(set1, set2):
    return sorted(set1 & set2)


cubs = [int(i) for i in input().split()]
notSame = set()
anny = set()
borya = set()
same = []
for i in range(cubs[0]):
    a = int(input())
    notSame.add(a)
    anny.add(a)
for i in range(cubs[1]):
    a = int(input())

    if a in notSame:
        anny.remove(a)
        same.append(a)
    else:
        notSame.add(a)
        borya.add(a)
print(len(same))
print(*sorted(same))
drAnny = drugie(anny, notSame)
drBorya = drugie(borya, notSame)
print(len(drAnny))
print(*drAnny)
print(len(drBorya))
print(*drBorya)
