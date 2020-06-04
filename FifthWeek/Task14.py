a = input().split()
sum = 0
for i in range(0, len(a)):
    if int(a[i]) > 0:
        sum += 1
print(sum)
