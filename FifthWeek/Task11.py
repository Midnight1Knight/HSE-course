firstNumber = int(input())
secondNumber = int(input())
for i in range(firstNumber, secondNumber + 1):
    if (i // 1000) == (i % 10) and (i // 100 % 10) == (i // 10 % 10):
        print(i)
