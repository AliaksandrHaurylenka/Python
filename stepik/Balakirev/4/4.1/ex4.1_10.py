num = list(map(int, (input())))
# print(num)

sum1 = sum(num[:3])
sum2 = sum(num[3:])

if sum1 == sum2:
    print('ДА')
else:
    print('НЕТ')


