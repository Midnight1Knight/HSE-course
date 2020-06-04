n = int(input())
sortList = [['', 0]] * n
for i in range(n):
    lineList = input().split()
    sortList[i] = lineList
sortList.sort(key=lambda x: int(x[1]), reverse=True)
for i in range(n):
    print(sortList[i][0], end=" ")
