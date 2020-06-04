num = int(input())
if 10 < num < 20:
    print(num, 'korov')
elif num % 10 == 0:
    print(num, 'korov')
elif num % 10 == 5:
    print(num, 'korov')
elif num % 10 == 6:
    print(num, 'korov')
elif num % 10 == 7:
    print(num, 'korov')
elif num % 10 == 8:
    print(num, 'korov')
elif num % 10 == 9:
    print(num, 'korov')
elif (num % 10) == 1:
    print(num, 'korova')
else:
    print(num, 'korovy')
