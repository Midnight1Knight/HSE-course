list1 = [int(i) for i in input().split()]
sumnum = len(list1)
for i in range(1, len(list1)):
    if list1[i - 1] == list1[i]:
        sumnum -= 1
print(sumnum)
