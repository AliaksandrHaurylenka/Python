# ex5.3_1
# num = []
# for i in range(11):
#     num.append(i)
#
# print(*num)


# ex5.3_2
# num = []
# for i in range(10, -1, -1):
#     num.append(i)
#
# print(*num)


# ex5.3_3
# num = []
# for i in range(-10, 0, 2):
#     num.append(i)
#
# print(*num)


# ex5.3_4
# num = []
# for i in range(1, 20, 3):
#     num.append(i)

# print(*num)


# ex5.3_5
# num = list(map(int, input().split()))
# print(num)
#
# # num_abs = []
# # for i in range(len(num)):
# #     num_abs.append(abs(num[i]))
# #
# # print(num_abs)
#
# # s = 0
# # for i in range(len(num_abs)):
# #     if num_abs[i] % 2 != 0:
# #         s += num_abs[i]
# #
# # print(s)
#
# # В задании предположил, что надо только положительные числа,
# # но этого не надо делать, т.е. переводить по модулю.
# s = 0
# for i in range(len(num)):
#     if num[i] % 2 != 0:
#         s += num[i]
#
# print(s)


# ex5.3_6
# cities = list(map(str, input().split()))
#
# num = []
# for i in range(len(cities)):
#     num.append(len(cities[i]))
#
# print(*num)


# ex5.3_7
# n = int(input())
#
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)


# ex5.3_8
# n = int(input())

# Приведенное решение задачи также исключает 1 из принятия ее за простое число,
# т.к. единица не является ни простым, ни составным числом и принимает один лишь делитель 1
# res = [1]
# for i in range(2, n + 1):
#     if i % n == 0 and n % i == 0:
#         res.append(i)
#         break
#     elif n % i == 0:
#         res.append(i)
#
# # print(res)
#
# if len(res) == 2:
#     print('ДА')
# else:
#     print('НЕТ')


# ex5.3_9
# Москва Астрахань Новгород Димитровград Душанбе
# cities = list(map(str, input().split()))
#
# cities_lower = []
# for i in range(len(cities)):
#     cities_lower.append(cities[i].lower())
#
# # print(cities_lower)
# # print(cities_lower[0][-1])
# # print(cities_lower[0][0])
#
# letters = ['ь', "ъ", "ы"]
# res = 'ДА'
# for i in range(len(cities_lower) - 1):
#     letter = cities_lower[i][-1]
#     if letter in letters:
#         letter = cities_lower[i][-2]
#
#     if letter != cities_lower[i + 1][0]:
#         res = 'НЕТ'
#         break
#
# print(res)


# ex5.3_10
n = int(input())

s = 0
for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        s += i

print(s)



