p = int(input())
x = int(input())
y = int(input())
xy = x * 100 + y
year = xy * p / 100 + xy
x = year // 100
y = year % 100
print(int(x), int(y))
