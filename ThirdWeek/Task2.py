n = int(input())
i = 1
a = n
b = 0
while i != a + 1:
    n = (1 / i**2)
    b += n
    i += 1
print(b)
