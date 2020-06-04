list1 = [int(i) for i in input().split()]
max1 = max(list1)
list1.pop(list1.index(max(list1)))
max2 = max(list1)
min1 = min(list1)
list1.pop(list1.index(min(list1)))
min2 = min(list1)
if max1 * max2 >= min1 * min2:
    print(max2, max1)
else:
    print(min1, min2)
