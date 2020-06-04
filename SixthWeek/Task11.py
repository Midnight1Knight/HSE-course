class SchoolBoy:
    name = ''
    surname = ' '
    rang = 0
    point = 0


inFile = open('input.txt', 'r', encoding='utf8')
max = [0] * 3
student = SchoolBoy()
for line in inFile:
    line = line.split()
    student.name = line[0]
    student.surname = line[1]
    student.rang = line[2]
    student.point = line[3]
    if max[11 - int(student.rang)] <= int(student.point):
        max[11 - int(student.rang)] = int(student.point)
print(*max[::-1])
inFile.close()
