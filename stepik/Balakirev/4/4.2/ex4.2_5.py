month = int(input())

if month == 1:
    print(31)
elif month == 2:
    print(28)
elif month == 3:
    print(31)
elif month == 4:
    print(30)
elif month == 5:
    print(31)
elif month == 6:
    print(30)
elif month == 7:
    print(31)
elif month == 8:
    print(31)
elif month == 9:
    print(30)
elif month == 10:
    print(31)
elif month == 11:
    print(30)
elif month == 12:
    print(31)


# Решения других
year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
num = int(input())
if 1 <= num <= 12:
    print(year[num - 1])
else:
    print('Введите число от 1 до 12')
