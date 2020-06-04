def min4(a, b, c, d):
    e = min(a, b)
    f = min(c, d)
    m = min(e, f)
    return m


first = int(input())
second = int(input())
third = int(input())
fourth = int(input())
print(min4(first, second, third, fourth))
