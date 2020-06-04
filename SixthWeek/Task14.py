class SchoolBoy:
    point0 = 0
    point1 = 0
    point2 = 0


def listing(student):
    sortList = []
    for sign in student:
        if sign.isdigit():
            sortList.append(int(sign))
        else:
            continue
    return sortList


def goden(point1, point2, point3):
    if int(point1) >= 40 and int(point2) >= 40 \
            and int(point3) >= 40:
        return True
    else:
        return False


inFile = open('input.txt', 'r', encoding='utf-8')
student = SchoolBoy()
listOfStudents = []
k = int(inFile.readline())
for line in inFile:
    splitLine = line.split()
    points = listing(splitLine)
    student.point0 = points[0]
    student.point1 = points[1]
    student.point2 = points[2]
    if goden(points[0], points[1], points[2]):
        sumOfPoints = sum(points)
        listOfStudents.append(sumOfPoints)
    else:
        continue
if len(listOfStudents) <= k:
    print(0)
elif k == 0:
    print(0)
elif len(listOfStudents) == 0:
    print(1)
else:
    listOfStudents.sort(reverse=True)
    countOfSame = [0] * 301
    for i in range(k + 1):
        countOfSame[listOfStudents[i]] += 1
    abit = 0
    lastPlace = 0
    for i in reversed(range(301)):
        if countOfSame[i] == 0:
            continue
        if abit + countOfSame[i] < k:
            abit += countOfSame[i]
            lastPlace = i
        elif abit + countOfSame[i] == k:
            print(i)
            break
        else:
            if abit + countOfSame[i] > k and abit == 0:
                print(1)
                break
            else:
                print(lastPlace)
                break
        if countOfSame[i] + abit > abit + k:
            print(1)
            break
inFile.close()
