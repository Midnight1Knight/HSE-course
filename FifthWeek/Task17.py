def IsAscending(A):
    i = 1
    while i <= len(A) - 1 and A[i] > A[i - 1]:
        i += 1
    return 'YES' if i == len(A) else 'NO'


A = list(map(int, input().split()))
print(IsAscending(A))
