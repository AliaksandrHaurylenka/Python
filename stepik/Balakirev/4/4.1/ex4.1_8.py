# cities = list(map(str, input().split()))
cities = list(map(str, input().split()))
# print(cities)

if "Москва" in cities:
    cities.remove("Москва")

print(*cities)
