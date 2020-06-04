list1 = [int(s) for s in input().split()]
place = [int(c) for c in input().split()]
list1.append(place[1])
for i in range(len(list1) - 1, place[0], -1):
    list1[i] = list1[i - 1]
list1[place[0]] = place[1]
print(' '.join([str(i) for i in list1]))
