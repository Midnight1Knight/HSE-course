n = int(input())
factrorial = 1
sum = 0
for i in range(1, n + 1):
    factrorial *= i
    sum += factrorial
print(sum)
