num1 = int(input())
num2 = int(input())
while num1 > num2:
    if (num1 // 2 >= num2) and (num1 % 2 == 0):
        num1 /= 2
        print(":2")
    else:
        num1 -= 1
        print("-1")
