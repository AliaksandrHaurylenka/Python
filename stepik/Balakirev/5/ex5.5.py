# ex5.5_2
# cities = list(map(str, input().split()))
#
# lst = iter(cities)
# print(next(lst))
# print(next(lst))


# ex5.5_3
# string = input()
#
# ch = iter(string)
# for i in range(len(string)):
#     a = next(ch)
#     if a == ' ':
#         break
#     else:
#         print(a, end='')


# ex5.5_4
num = str(input())
# print(num)

it = iter(num)
# print(next(it))

for i in range(len(num)):
    # a = next(it)
    # print(a + ' ', end='')
    print(next(it) + ' ', end='')


