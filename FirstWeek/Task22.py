num = int(input())
n1 = num // 1000
n2 = num // 100 % 10
n3 = num // 10 % 10
n4 = num % 10
num1 = str(n1) + str(n2)
num2 = str(n4) + str(n3)
print((int(num1) - int(num2)) + 1)
