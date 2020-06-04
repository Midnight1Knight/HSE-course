class SchoolBoy:
    name = ''
    surname = ' '
    rank = 0
    points = 0


inFile = open('input.txt', 'r', encoding='utf-8')
winers = [0] * 3
maxPoints = [0] * 3
student = SchoolBoy()
for i in inFile:
    fileList = i.split()
    student.name = fileList[0]
    student.surname = fileList[1]
    student.rank = fileList[2]
    student.points = fileList[3]
    if maxPoints[abs(9 - int(student.rank))] < int(student.points):
        winers[abs(9 - int(student.rank))] = 1
        maxPoints[abs(9 - int(student.rank))] = int(student.points)
    elif maxPoints[abs(9 - int(student.rank))] == int(student.points):
        winers[abs(9 - int(student.rank))] += 1
print(*winers)
inFile.close()
