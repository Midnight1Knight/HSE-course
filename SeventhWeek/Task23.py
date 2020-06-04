inFile = open('input.txt', 'r', encoding='utf-8')
bank = {}
for line in inFile:
    line = line.split()
    operation = str(line[0])
    name = str(line[1])
    if operation == 'DEPOSIT':
        money = int(line[-1])
        bank.setdefault(name, 0)
        bank[name] += int(money)
    elif operation == 'WITHDRAW':
        money = int(line[-1])
        bank.setdefault(name, 0)
        bank[name] -= int(money)
    elif operation == 'BALANCE':
        try:
            print(bank[name])
        except:
            print('ERROR')
    elif operation == 'TRANSFER':
        name2 = line[2]
        money = line[-1]
        bank.setdefault(name, 0)
        bank.setdefault(name2, 0)
        bank[name] -= int(money)
        bank[name2] += int(money)
    elif operation == 'INCOME':
        percent = int(name)
        for account in bank:
            if bank[account] >= 0:
                bank[account] += bank[account] * percent // 100
            else:
                continue
