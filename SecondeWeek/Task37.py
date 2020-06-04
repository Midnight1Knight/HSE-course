now = int(input())
i = 0
a = now
while now != 0:
    if a < now:
        i += 1
    a = now
    now = int(input())
print(i)
