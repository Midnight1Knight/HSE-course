num = int(input())
plenty = set(range(1, num + 1))
while True:
    ques = input()
    if ques == 'HELP':
        break
    ques = {int(c) for c in ques.split()}
    answr = str(input())
    if answr == 'YES':
        plenty &= ques
    if answr == 'NO':
        plenty -= ques
print(*sorted(plenty))
