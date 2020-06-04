a = input().split()
mx = [0, 0]
for i in range(0, len(a)):
    if int(mx[0]) <= int(a[i]):
        mx = [a[i], i]
print(*mx)
