beg = int(input())
end = int(input())
if end % (end - beg + 1) == 0:
    print("YES")
else:
    print("NO")
