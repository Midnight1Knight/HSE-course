def sequence():
    num = int(input())
    if num == 0:
        return 0
    else:
        return num + sequence()


print(sequence())
