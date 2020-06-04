h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
h1 = h1 * 3600
h2 = h2 * 3600
m1 = m1 * 60
m2 = m2 * 60
r1 = h1 + m1 + s1
r2 = h2 + m2 + s2
r = r2 - r1
print(r)
