num = input()
lst_num = list(map(int, num))
print(lst_num)
print(sum(lst_num))
len_lst_num = len(lst_num)
print(len_lst_num)

i = 1
sum_num = 1
while i <= len_lst_num:
    sum_num *= lst_num[i - 1]
    i += 1

print(sum_num)

