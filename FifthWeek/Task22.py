a = [int(i) for i in input().split()]
for i in range(0, len(a)):
    if a[i] % 2 != 0:
        mn = a[i]
for i in range(0, len(a)):
    if a[i] % 2 != 0 and a[i] < mn:
        mn = a[i]
print(mn)
