i = 1
n = float(input())
x = float(input())
res = 0
while i != n + 1:
    a = float(input())
    res = res * x + a
    i += 1
print(res)
