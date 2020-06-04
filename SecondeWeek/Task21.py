a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == b == 0:
    print("INF")
elif a == 0 or b % a != 0 or c * (-b / a) + d == 0:
    print("NO")
else:
    print(-b // a)
