k = int(input())

weekday = ['понедельник', "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

print(k % 7)

if 1 <= k <= 365:
    if k == 1 or k % 7 == 1:
        print(weekday[0])
    elif k == 2 or k % 7 == 2:
        print(weekday[1])
    elif k == 3 or k % 7 == 3:
        print(weekday[2])
    elif k == 4 or k % 7 == 4:
        print(weekday[3])
    elif k == 5 or k % 7 == 5:
        print(weekday[4])
    elif k == 6 or k % 7 == 6:
        print(weekday[5])
    elif k == 7 or k % 7 == 7:
        print(weekday[6])
else:
    print('к должно быть  в диапазоне от 1 до 365')


# Другие решения
n = int(input())
lst = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

print(lst[n % 7 - 1])

