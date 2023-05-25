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
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
print(lst_in)  # Чтобы закончить ввод, необходимо нажать Ctrl + D

# здесь продолжайте программу (используйте список lst_in)
# django chto  eto takoe    poryadok ustanovki
# model mtv   marshrutizaciya funkcii  predstavleniya
# marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya

for row in lst_in:
    # row = row.replace('  ', ' ')
    # print(row)

    double_space_count = row.count('  ')
    # print(double_space_count)

    for i in range(double_space_count):
        row = row.replace('  ', ' ')

    row = row.replace(' ', '-')

    print(row)



# ex5.6_3


# ex5.6_4


# ex5.6_5


# ex5.6_6


# ex5.6_7


# ex5.6_8
