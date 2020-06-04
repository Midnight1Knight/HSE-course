from math import sqrt


def MinDivisor(n):
    i = 2
    while n % i != 0:
        if i >= sqrt(n):
            print(n)
            return
        i += 1
    print(i)


n = int(input())
MinDivisor(n)
