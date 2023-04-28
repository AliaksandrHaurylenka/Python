# ex5.6_1
# N = int(input())
#
# lst = []
# for i in range(N):
#     lst.append([1] * N)
#     for j in range(N):
#         lst[i][-1] = 5
#
#     print(*lst[i])


# ex5.6_2
# import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# for row in lst_in:
#     # row = row.replace('  ', ' ')
#     # print(row)
#
#     double_space_count = row.count('  ')
#     # print(double_space_count)
#
#     for i in range(double_space_count):
#         row = row.replace('  ', ' ')
#
#     row = row.replace(' ', '-')
#
#     print(row)


# ex5.6_3
# n = int(input())
#
# lst = []
# for i in range(2, n):
#     # print(i, end=' ')
#
#     lst_len_two = [1]
#     for j in range(2, i + 1):
#         if i % j == 0:
#             lst_len_two.append(i)
#
#     if len(lst_len_two) < 3:
#         lst.append(i)
#
# print(*lst)


# ex5.6_4
# import sys
#
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# # 1 0 0 0 0
# # 0 0 1 0 1
# # 0 0 0 0 0
# # 0 1 0 1 0
# # 0 0 0 0 0
# print(lst_in)

# здесь продолжайте программу (используйте список lst_in)


# ex5.6_5
# import sys
#
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# # 2 3 4 5 6
# # 3 2 7 8 9
# # 4 7 2 0 4
# # 5 8 0 2 1
# # 6 9 4 1 2
# print(lst_in)
# здесь продолжайте программу (используйте список lst_in)


# ex5.6_6
# Import time module
# import time
#
# num = list(map(int, input().split()))
# # 8 11 -53 2 10 11
# # print(num)
#
# # record start time
# start = time.time()
#
# for i in range(len(num)):
#     # Мое решение
#     # for j in range(len(num)):
#     #     if num[j] > num[i]:
#     #         num[j], num[i] = num[i], num[j]
#
#     # Другое решение работает гораздо быстрее из-за выхода из итерации при помощи continue.
#     for j in range(i, len(num)):
#         if num[i] < num[j]:
#             continue
#         else:
#             num[i], num[j] = num[j], num[i]
#
# print(*num)
#
# # record end time
# end = time.time()
#
# # print the difference between start
# # and end time in milli. secs
# print("The time of execution of above program is :",
#       (end - start) * 10 ** 3, "ms")


# ex5.6_7
# num = list(map(int, input().split()))
# # 4 5 2 0 6 3 -56 3 -1
#
# for i in range(len(num)):
#     for j in range(len(num) - 1):
#         if num[j] < num[j + 1]:
#             continue
#         else:
#             num[j], num[j + 1] = num[j + 1], num[j]
#
# print(*num)


# ex5.6_8
# Import time module
import time

n = int(input())
# banknotes = [1, 2, 4, 8, 16, 32, 64]
banknotes = [64, 32, 16, 8, 4, 2, 1]

# record start time
start = time.time()

# Мое решение работает быстрее
lst = []
for i in range(len(banknotes)):
    a = n // banknotes[i]

    for j in range(0, a):
        lst.append(banknotes[i])

    n = n % banknotes[i]

print(*lst)

# record end time
end = time.time()

print('\n')
# # print the difference between start
# # and end time in milli. secs
print("The time of execution of above program is :",
      (end - start) * 10 ** 3, "ms")


n = int(input())
start = time.time()
# Другое решение
for i in banknotes:
    while n >= i:
        print(i, end=' ')
        n -= i

# record end time
end = time.time()

print('\n')
# # print the difference between start
# # and end time in milli. secs
print("The time of execution of above program is :",
      (end - start) * 10 ** 3, "ms")
