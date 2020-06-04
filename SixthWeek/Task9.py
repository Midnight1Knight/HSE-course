def CountSort(A):
    rtrn = str()
    cntA = [0] * 101
    for i in A:
        cntA[i] += 1
    for nowA in range(101):
        rtrn += ((str(nowA) + ' ') * cntA[nowA])
    return rtrn

list0 = map(int, input().split())
print(CountSort(list0))
