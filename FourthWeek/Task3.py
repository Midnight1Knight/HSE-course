from math import sqrt


def lent(x1, y1, x2, y2, x3, y3):
    l1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    l2 = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    l3 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    per = l1 + l2 + l3
    return per


a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
print('{:.6f}'.format(lent(a, b, c, d, e, f)))
