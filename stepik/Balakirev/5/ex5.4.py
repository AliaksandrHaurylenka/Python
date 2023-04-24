# ex5.4_1
# string = str(input())
# # Барабанщик бил бой в барабан
# ch = 'а'
# lst = []
# for i, c in enumerate(string):
#     # if not string[i + 1]:
#     #     break
#
#     if c == ch and string[i - 1] == 'р':
#         lst.append(i - 1)
# #         # print(i)
#
# if lst:
#     print(*lst)
# else:
#     print(-1)


# ex5.4_2
# tel = list(input("Введите телефон в формате +7(xxx)xxx-xx-xx: "))
# for i in range(3, 6):
#     tel[i] = int(tel[i])
#
# for i in range(7, 10):
#     tel[i] = int(tel[i])
#
# for i in range(11, 13):
#     tel[i] = int(tel[i])
#
# tel[14] = int(tel[14])
# tel[15] = int(tel[15])
# print(tel)
#
# res = 'НЕТ'
# if tel[0] == '+' and \
#         tel[1] == '7' and \
#         tel[2] == '(' and \
#         tel[6] == ')' and \
#         tel[10] == '-' and \
#         tel[13] == '-' and \
#         int(tel[3]) and \
#         len(tel) == 16:
#     res = 'ДА'
#
# print(res)


# num = input()
# phone_num = '+7(' + num[3:6] + ')' + num[7:10] + '-' + num[11:13] + '-' + num[14:]
# print(num)
# print(len(phone_num))
# print(phone_num)
#
# if len(phone_num) == 16 and num.isdigit():
#     print('ДА')
# else:
#     print("НЕТ")

# tel = input()
# tel = list(input("Введите телефон в формате +7(xxx)xxx-xx-xx: "))
# mask_tel = list('+7(xxx)xxx-xx-xx')
# # +7(123)456-78-99
#
# # for i in range(3, 6):
# #     tel[i] = int(tel[i])
# #
# # for i in range(7, 10):
# #     tel[i] = int(tel[i])
# #
# # for i in range(11, 13):
# #     tel[i] = int(tel[i])
# #
# # tel[14] = int(tel[14])
# # tel[15] = int(tel[15])
# print(tel)
# print(len(tel))
# print(mask_tel)
# print(len(mask_tel))
# print(tel[4].isdigit())
#
# res = "ДА"
# # if len(mask_tel) != len(tel):
# #     res = 'НЕТ'
# #     break
#
# i = 0
# # if len(mask_tel) != len(tel):
# #     res = 'НЕТ'
# #     break
# if (mask_tel[i] == 'x' and tel[i].isdigit()) or (mask_tel[i] != 'x' and tel[i] == mask_tel[i]):
#     # res = 'НЕТ'
#     i += 1
# else:
#     res = 'НЕТ'
#
# print(res)


# ex5.4_3
# 10 + 25 - 12
str_arithmetic = input()
str_arithmetic = eval(str_arithmetic)
print(str_arithmetic)

# Другие решения
text = input().replace(' ', '').replace('-', '+-').split('+')
print(text)
print(sum(map(int, text)))

# ex5.4_4
# ex5.4_5
# ex5.4_6
# ex5.4_7
