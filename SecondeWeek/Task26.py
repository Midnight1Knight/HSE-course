n = int(input())
i = 2
while True:
    if n % i != 0:
        i += 1
    else:
        print(i)
        break
