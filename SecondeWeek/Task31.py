now = int(input())
MaxNum = now
while now != 0:
    now = int(input())
    if MaxNum < now:
        MaxNum = now
print(MaxNum)
