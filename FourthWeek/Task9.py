def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


num = int(input())
if IsPrime(num):
    print("YES")
else:
    print("NO")
