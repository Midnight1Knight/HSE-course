def less(x):
    return int(x[0])


def less1(x):
    return int(x[1])


n = int(input())
nCor = input().split()
m = int(input())
mCor = input().split()
for i in range(n):
    nCor[i] = [nCor[i], i, 0]
for i in range(m):
    mCor[i] = [mCor[i], i, 0]
nCor.sort(key=less)
mCor.sort(key=less)
j = 0
start = 0
for i in range(n):
    minimun = 10e10
    for j in range(start, m):
        diff = abs(int(nCor[i][0]) - int(mCor[j][0]))
        if diff < minimun:
            start = j
            minimun = diff
            nCor[i][2] = mCor[j][1] + 1
        else:
            break
nCor.sort(key=less1)
for i in range(n):
    print(nCor[i][2], end=" ")
