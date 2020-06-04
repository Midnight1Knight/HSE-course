numOfStudents = int(input())
AllKnowLang = set()
knowAllStud = set()
intpt = int(input())
lst = []
for i in range(numOfStudents):
    if i == 0:
        for j in range(intpt):
            lang = str(input())
            knowAllStud.add(lang)
            AllKnowLang.add(lang)
        continue
    else:
        intpt = int(input())
        lst = []
        for m in range(intpt):
            lang = str(input())
            lst.append(lang)
        AllKnowLang -= knowAllStud ^ set(lst)
        knowAllStud |= set(lst)
print(len(AllKnowLang))
print(*AllKnowLang, sep="\n")
print(len((knowAllStud)))
print(*knowAllStud, sep="\n")
