list1 = [int(i) for i in input().split()]
for i in range(1, len(list1), 2):
    list1[i], list1[i - 1] = list1[i - 1], list1[i]
print(*list1)
