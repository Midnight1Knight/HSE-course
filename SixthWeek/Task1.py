def merge(a, b):
    c = []
    i, j = 0, 0
    allLists = list0 + list1
    lAllLists = len(allLists)
    lList0 = len(list0)
    lList1 = len(list1)
    while i + j < lAllLists:
        if i < lList0 and j < lList1:
            if list0[i] < list1[j]:
                c.append(list0[i])
                i += 1
            else:
                c.append(list1[j])
                j += 1
        elif i < lList0:
            c.append(list0[i])
            i += 1
        elif j < lList1:
            c.append(list1[j])
            j += 1
    return c


list0 = [int(n) for n in input().split()]
list1 = [int(n) for n in input().split()]
print(*merge(list0, list1))
