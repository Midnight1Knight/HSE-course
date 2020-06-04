def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def ReduceFraction(n, m):
    a = gcd(n, m)
    n //= a
    m //= a
    return n, m


p = int(input())
q = int(input())
print(*ReduceFraction(p, q))
