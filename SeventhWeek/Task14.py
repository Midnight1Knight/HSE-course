countries = int(input())
countyAndCity = dict()
for i in range(countries):
    now = [i for i in input().split()]
    for j in range(1, len(now)):
        countyAndCity[now[j]] = now[0]
cities = int(input())
for i in range(cities):
    city = str(input())
    print(countyAndCity.get(city))
