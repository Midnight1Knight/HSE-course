from math import sqrt


def distance(x1, y1, x2, y2):
    d = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return d


first = float(input())
second = float(input())
third = float(input())
fourth = float(input())
print(distance(first, second, third, fourth))
