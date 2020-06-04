class SchoolBoy:
    name = ''
    surname = ''
    numOfSchool = 0
    point = 0


inFile = open('input.txt', 'r', encoding='utf-8')
stud = SchoolBoy()
listOfSchool = [0] * 100
for line in inFile:
    infList = line.split()
    stud.name = infList[0]
    stud.surname = infList[1]
    stud.numOfSchool = infList[2]
    stud.point = infList[3]
    listOfSchool[int(stud.numOfSchool)] += 1
maxStudents = max(listOfSchool)
for i in range(len(listOfSchool)):
    if listOfSchool[i] == maxStudents:
        print(i, end=" ")
inFile.close()
