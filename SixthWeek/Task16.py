class SchoolBoy:
    name = ''
    surname = ' '
    rank = 0
    points = 0


inFile = open('input.txt', 'r', encoding='utf-8')
maxPoints = [0] * 3
preMax = [0] * 3
student = SchoolBoy()
for i in inFile:
    fileList = i.split()
    student.name = fileList[0]
    student.surname = fileList[1]
    student.rank = fileList[2]
    student.points = fileList[3]
    if maxPoints[abs(9 - int(student.rank))] < int(student.points):
        preMax[abs(9 - int(student.rank))] =\
            maxPoints[abs(9 - int(student.rank))]
        maxPoints[abs(9 - int(student.rank))] = int(student.points)
    elif (maxPoints[abs(9 - int(student.rank))] > int(student.points)) \
            and (preMax[abs(9 - int(student.rank))] < int(student.points)):
        preMax[abs(9 - int(student.rank))] = int(student.points)
print(*preMax)
inFile.close()
