freePlace = [int(i) for i in input().split()]
s = freePlace[0]
n = freePlace[1]
i = 0
a = []
sum = 0
kol = 0
while i < n:
    k = int(input())
    i += 1
    a.append(k)
a.sort()
for i in range(n):
    if sum + a[i] < s:
        sum += a[i]
        kol += 1
    else:
        break
print(kol)
