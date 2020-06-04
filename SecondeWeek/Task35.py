now = int(input())
i = 0
sm = now
while now != 0:
    now = int(input())
    sm += now
    i += 1
print(float(sm / i))
