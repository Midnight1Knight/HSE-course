n = int(input())
ot = 10**n - 1
if n == 1:
    do = 1
else:
    do = 10**(n - 1) + 1
for i in range(ot, do - 1, -2):
    print(i, end=" ")
