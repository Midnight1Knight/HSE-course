p = float(0)
n = int(input())
x = float(input())
sumX = float
counter = 0
while n > 0:
    k = float(input())
    sumX = x
    counter = n
    while counter > 1:
        sumX *= x
        counter -= 1
    p += float(k * sumX)
    n -= 1
k = float(input())
p += float(k)
print(float(p))
