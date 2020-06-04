list1 = [int(i) for i in input().split()]
list0 = []
list123 = []
for i in range(len(list1)):
    if list1[i] == 0:
        list0.append(0)
    else:
        list123.append(list1[i])
print(*list123 + list0)
