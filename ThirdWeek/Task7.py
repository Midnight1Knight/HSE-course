p = int(input())
x = int(input())
y = int(input())
k = int(input())
i = 0
xy = x * 100 + y

while i != k:
    xy += xy * p // 100
    i += 1
x = xy // 100
y = xy % 100
print(int(x), int(y))
