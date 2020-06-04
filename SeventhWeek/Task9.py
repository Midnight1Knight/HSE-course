num = int(input())
plenty = set(range(1, num + 1))
while True:
    ques = input()
    if ques == 'HELP':
        break
    else:
        ques = {int(x) for x in ques.split()}
    if len(ques & plenty) <= len(plenty) // 2:
        print('NO')
        plenty -= ques
    elif len(ques & plenty) > len(plenty) // 2:
        print('YES')
        plenty &= ques
print(*sorted(plenty))
