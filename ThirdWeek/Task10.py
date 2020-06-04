from math import *
x = 4
n = -1
s = 0
summa = 0
xx = 0
while x != 0:
    x = int(input())
    summa += x
    n += 1
    xx = xx + x * x
s = summa / n
q = sqrt((xx + s * s * n - 2 * summa * s) / (n - 1))
print(q)
