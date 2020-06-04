v1 = int(input())
g1 = int(input())
v2 = int(input())
g2 = int(input())
if (g2 > g1 and
        g2 - g1 >= abs(v2 - v1) and
        ((v1 % 2 == v2 % 2 and (g2 - g1) % 2 == 0) or
         (v1 % 2 != v2 % 2 and (g2 - g1) % 2 != 0)) and
        min(g1, g2, v1, v2) > 0 and
        max(g1, g2, v1, v2) < 9):
    print('YES')
else:
    print('NO')
