days, parties = map(int, input().split())
daysWork = set()
repeat = []

for i in range(0, parties):
    base, step = map(int, input().split())
    if [base, step] not in repeat:
        repeat.append([base, step])
        daysWork |= {int(i) for i in range(base, days + 1, step)
                     if i % 7 not in [0, 6]}
print(len(daysWork))
