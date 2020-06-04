def null(n):
    s = 0
    while n != 0:
        num = int(input())
        if num == 0:
            s += 1
        n -= 1
    return s


n = int(input())
print(null(n))
