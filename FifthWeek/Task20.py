a = [int(i) for i in input().split()]
mn = 1000
for i in range(0, len(a)):
    if 0 < a[i] < mn:
        mn = a[i]
print(mn)
