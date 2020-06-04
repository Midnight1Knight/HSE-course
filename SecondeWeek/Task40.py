num = int(input())
i = 1
fib1 = fib2 = 1
a = 1
while i != num:
    a = fib2
    fib2 = fib1
    fib1 = fib2 + a
    i += 1
print(fib2)
