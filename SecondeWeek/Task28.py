n = int(input())
i = 1
while i <= n:
    if i == n:
        print("YES")
        break
    else:
        i *= 2
if i > n:
    print("NO")
