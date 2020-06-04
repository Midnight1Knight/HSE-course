list1 = [i for i in input().split()]
save = list1[-1]
for i in range(1, len(list1)):
    list1[- i], list1[- i - 1] = list1[- i - 1], list1[- i]
print(*list1)
