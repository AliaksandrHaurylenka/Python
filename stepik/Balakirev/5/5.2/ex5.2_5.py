cities = list(map(str, input().split()))
# print(cities)

i = 0
string = "ДА"
while i < len(cities):
    if len(cities[i]) > 5:
        i += 1
    else:
        string = 'НЕТ'
        break

# Самара Ульяновск Новгород Воронеж
print(string)

