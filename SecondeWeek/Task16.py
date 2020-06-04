a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print("3")
elif (a == b) or (a == c) or (c == b):
    print("2")
else:
    print("0")
