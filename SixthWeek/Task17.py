kilometers = [int(i) for i in input().split()]
taxis = [int(i) for i in input().split()]
kilometers.sort()
taxis.sort(reverse=True)
amount = 0
for i in range(len(taxis)):
    amount += kilometers[i] * taxis[i]
print(amount)
