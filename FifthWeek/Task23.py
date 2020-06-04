num = list(input().split())
for i in range(0, (len(num) + 1) // 2):
    midlle = num[-i - 1]
    num[-i - 1] = num[i]
    num[i] = midlle
print(*num)
