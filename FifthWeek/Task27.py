height = [int(i) for i in input().split()]
petya = int(input())
place = 0
for i in range(0, len(height)):
    if place < len(height) and petya <= height[place]:
        place += 1
    else:
        break
print(place + 1)
