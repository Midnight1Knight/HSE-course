def power(a, n):
    i = 1
    b = a
    while i != n:
        if n < 0:
            b = 1 / (a * a)
        elif n == 0:
            b = 1
            break
        else:
            b *= a
        i += 1
    print(b)


a1 = float(input())
n1 = float(input())
power(a1, n1)
