def kegli(nk):
    list1 = ["I"] * nk[0]
    for i in range(0, nk[1]):
        lr = [int(j) for j in input().split()]
        for j in range(lr[0] - 1, lr[1]):
            list1.pop(j)
            list1.insert(lr[0] - 1, ".")
    return list1


nk = [int(i) for i in input().split()]
print("".join(kegli(nk)))
