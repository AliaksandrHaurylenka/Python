# ex5.8_1

# 5.56 -8.7 1.0 3.14 77.845
# lst = [abs(float(i)) for i in input().split()]
# print(lst)


# ex5.8_2

# 4567397
# num_str = input()
# lst = [int(num) for num in num_str]
#
# print(lst)


# ex5.8_3

# N = int(input())
#
# lst = [[0] * N for x in range(N)]
#
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             lst[i][j] = 1
#
# # print(*lst, sep='\n')
# a = [print(*i) for i in lst]


# ex5.8_4

# Казань Уфа Москва Челябинск Омск Тур Самара
# cities = list(map(str, input().split()))
# # print(*cities)
#
# lst = [print(i, end=' ') for i in cities if len(i) > 5]
# print(lst)


# ex5.8_5

# Подвиг 5. Вводится натуральное число n.
# Необходимо сформировать список с помощью list comprehension,
# состоящий из делителей числа n (включая и само число n).
# Результат вывести на экран в одну строку через пробел.

# Sample Input: 10
# Sample Output: 1 2 5 10

# n = int(input())
#
# print(*[i for i in range(1, n + 1) if n % i == 0])


# ex5.8_6

# Подвиг 6. Вводится натуральное число N.
# Необходимо сгенерировать вложенный список с помощью list comprehension, размером N x N,
# где первая строка содержала бы все нули, вторая - все единицы, третья - все двойки и так до N-й строки.
# Результат вывести в виде таблицы чисел как показано в примере ниже.

# Sample Input:
#
# 4
# Sample Output:
#
# 0 0 0 0
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3

# n = int(input())
#
# # print(*[[i]  * n for i in range(n)] , sep='\n')
#
# lst = [[i] * n for i in range(n)]
#
# a = [print(*i) for i in lst]


# ex5.8_7

# Вводится список вещественных чисел.
# С помощью list comprehension сформировать список,
# состоящий из элементов введенного списка, имеющих четные индексы
# (то есть, выбрать все элементы с четными индексами).
# Результат вывести на экран в одну строку через пробел.

# Sample Input:
#
# 8.5 11.3 1.0 -4.5 11.34 6.45
# Sample Output:
#
# 8.5 1.0 11.34

# lst = [float(i) for i in input().split()]
#
# print(*lst[0::2])


# ex5.8_8

# Вводятся два списка целых чисел одинаковой длины каждый с новой строки.
# С помощью list comprehension сформировать третий список,
# состоящий из суммы соответствующих пар чисел введенных списков.
# Результат вывести на экран в одну строку через пробел.

# Sample Input:
#
# 1 2 3 4 5
# 6 7 8 9 10
#
# Sample Output:
#
# 7 9 11 13 15

# a = [int(i) for i in input().split()]
#
# b = [int(i) for i in input().split()]
#
# # print(*a)
#
# # print(*b)
#
# # c = a + b
#
# # print(*c)
#
# d = [a[i] + b[i] for i in range(len(a))]
#
# print(*d)


# ex5.8_9

# Вводится список в формате:

# <город 1> <численность населения 1> <город 2> <численность населения 2> ...
# <город N> <численность населения N>

# Необходимо с помощью list comprehension сформировать список lst, содержащий вложенные списки из пар:

# <город> <численность населения>

# Численность населения - целое число в тыс. человек.
# Вывести результат на экран в виде списка командой:
#
# print(lst)
#
# Sample Input:
# Москва 15000 Уфа 1200 Самара 1090 Казань 1300
#
# Sample Output:
# [['Москва', 15000], ['Уфа', 1200], ['Самара', 1090], ['Казань', 1300]]

cities = [i for i in input().split()]

# Москва 15000 Уфа 1200 Самара 1090 Казань 1300

# print(cities)

a = [int(cities[i]) if i % 2 != 0 else str(cities[i]) for i in range(len(cities))]

# print(a)

# b = [[cities[i] + cities[i + 1]] for i in range(0, len(a), 2)]

# print(b)

b = [[a[i], a[i + 1]] for i in range(0, len(a), 2)]

print(b)
