# quantity_books = int(input('Введите количество книг в списке: '))
# print('Введите названия книг:')
#
# lst_books = []
# i = 0
# while i < quantity_books:
#     book = input()
#     lst_books.append(book)
#
#     i += 1
#
# print(lst_books)
#
# j = 0
# while j < len(lst_books):
#     a = len(lst_books[j].split())
#     if a >= 2:
#         del lst_books[j]
#
#     j += 1
#
# print(*lst_books)


import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
# для прерывания ввода, чтобы продолжился код дальше, необходимо нажать Ctrl + D

# здесь продолжайте программу (используйте список lst_in)
# print(lst_in)
# print(len(lst_in))

j = 0
while j < len(lst_in):
    a = lst_in[j].count(" ") + 1
    print(a)
    if a > 1:
        del lst_in[j]
    else:
        j += 1

# dfgsdgs
# dfgdfg shsth
# cgyjc gfhf xthxth
# # xfthxfth gxfh hfhft fthfth
print(lst_in)

