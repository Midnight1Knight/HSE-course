def mult(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return a * mult(a, n - 1)
    else:
        return a * mult(a * a, n // 2)


a = float(input())
n = float(input())
print(mult(a, n))
