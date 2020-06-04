now = int(input())
i = 1
nex = now
a = i
while now != 0:
    if (nex + 1) == now or (nex - 1) == now:
        i += 1
    if a < i:
        a = i
    if (nex + 1) != now or (nex - 1) != now or now == nex:
        i = 1
    nex = now
    now = int(input())
print(a)
