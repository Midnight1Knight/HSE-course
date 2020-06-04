used = set()
for i in input().split():
    n = int(i)
    if n in used:
        print('YES')
    else:
        print('NO')
        used.add(n)
