def conversely():
    n = int(input())
    if n != 0:
        conversely()
        print(n)


print("0")
conversely()
