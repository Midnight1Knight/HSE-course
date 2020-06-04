yourSize = int(input())
sizes = [int(i) for i in input().split()]
sizes.sort()
num = 0
j = 0
sum = 0
kol = 0
for i in range(len(sizes)):
    if sizes[i] >= yourSize:
        num += 1
        j = i + 1
        sum = sizes[i]
        break
    kol = i
if kol == len(sizes) - 1 and num == 0:
    num = 0
else:
    while j < len(sizes):
        if sizes[j] >= sum + 3:
            num += 1
            sum = sizes[j]
        j += 1

print(num)
