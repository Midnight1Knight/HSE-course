class SchoolBoy:
    name = ''
    surname = ' '
    rank = 0
    points = 0


f = open('input.txt', 'r', encoding='utf-8')
allPoints = [0, 0, 0]
allRanks = [0, 0, 0]
ranks = 0
for line in f:
    iLine = line.split()
    student = SchoolBoy()
    student.name = iLine[0]
    student.surname = iLine[1]
    student.rank = iLine[2]
    student.points = iLine[3]
    if int(student.rank) != ranks + 9:
        ranks += (int(student.rank) - (9 + ranks))
    allPoints[ranks] += int(student.points)
    allRanks[ranks] += 1
for i in range(len(allPoints)):
    print('{:.10f}'.format(allPoints[i] / allRanks[i]), end=" ")
f.close()
