def power(a, b):
    if a == 0:
        return b
    a -= 1
    b += 1
    if a > 0:
        return power(a, b)
    else:
        return b


a1 = int(input())
b1 = int(input())
print(power(a1, b1))
