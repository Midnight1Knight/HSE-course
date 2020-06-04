buses = [int(i) for i in input().split()]
firstBus = set()
secondBus = set()
bus1 = []
bus2 = []
bus1.append(buses[0])
bus1.append(buses[1])
bus2.append(buses[2])
bus2.append(buses[3])
bus1.sort()
bus2.sort()
for i in range(bus1[0], bus1[1] + 1):
    firstBus.add(i)
for i in range(bus2[0], bus2[1] + 1):
    secondBus.add(i)
print(len(firstBus & secondBus))
