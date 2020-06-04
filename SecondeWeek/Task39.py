now = int(input())
i = 0
max1 = now
while now != 0:
    if max1 < now:
        i = 0
        max1 = now
    if max1 == now:
        i += 1
    now = int(input())
print(i)
