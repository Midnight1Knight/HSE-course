n = int(input())
progression = ((1 + n) * n) // 2
sum = 0
for i in range(1, n):
    num = int(input())
    sum += num
residue = progression - sum
print(residue)
