def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


a1 = float(input())
n1 = float(input())
print(power(a1, n1))
