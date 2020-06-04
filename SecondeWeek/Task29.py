n = int(input())
i = 1
while n != 1:
    if n % 2 != 0:
        n += 1
    n /= 2
    i += 1
print(i - 1)
