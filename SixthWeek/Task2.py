def Intersection(A, B):
    i = j = 0
    C = []
    while i + j < len(A) + len(B):
        if A[-1] < B[j] or len(A) == i:
            break
        if B[-1] < A[i] or len(B) == j:
            break
        if A[i] == B[j]:
            C.append(A[i])
            if i >= j:
                i += 1
            else:
                j += 1

        elif A[i] > B[j]:
            j += 1
        elif A[i] < B[j]:
            i += 1
    return C


A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
print(*Intersection(A, B))
