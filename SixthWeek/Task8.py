class SchoolBoy:
    name = ''
    surname = ' '
    numOfTheSchool = 0
    points = 0


inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
student = SchoolBoy()
students = []
for line in inFile:
    line = line.split()
    student.name = line[0]
    student.surname = line[1]
    student.numOfTheSchool = line[2]
    student.points = line[3]
    students.append([student.name, student.surname,
                     student.points])
students.sort(key=lambda x: x[0])
for i in range(len(students)):
    print(*students[i], file=outFile)
inFile.close()
outFile.close()
