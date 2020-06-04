r = int(input())
k = int(input())
c = int(input())
k = k + r * 100
c = k * c
r = c // 100
k = c % 100
print(r, k)
