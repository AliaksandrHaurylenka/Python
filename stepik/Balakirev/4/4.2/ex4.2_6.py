number_of_days_in_a_month_of_the_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# m_figure = [10, 11, 12]
# n_figure = [28, 30, 31]
m, n = map(int, input().split())
# m = int(input())
# n = int(input())
# m, n = int(input()), int(input())
# print(m, n)
# print(type(m))
# print(f'0{m}.{n-1} 0{m}.{n+1}')

# if m in figure:
#     print(f'{m}.{n - 1} {m}.{n + 1}')
# else:
#     print(f'0{m}.{n - 1} 0{m}.{n + 1}')

# if m in m_figure:
#     if n in n_figure:
#         print(f'{m}.{n-1} {m+1}.01')
#     else:
#         print(f'{m}.{n - 1} {m}.{n + 1}')
# else:
#     if n in n_figure:
#         print(f'{m}.{n - 1} {m + 1}.01')
#     else:
#         print(f'0{m}.{n - 1} 0{m}.{n + 1}')


# if 10 <= m <= 12:
#     if n in n_figure:
#         print(f'{m}.{n-1} {m+1}.01')
# elif 1 <= m <= 9:
#     if n in n_figure:
#         print(f'0{m}.{n - 1} 0{m + 1}.01')
#     else:
#         print(f'0{m}.{n - 1} 0{m}.{n + 1}')
# else:
#     print('Число месяца должно быть от 1 до 12')

# print(number_of_days_in_a_month_of_the_year[m - 1])

if 10 <= m <= 12:
    if m == 12 and n == 31:
        print('31 декабря в расчет не должно входить!')
        exit()
    if n == number_of_days_in_a_month_of_the_year[m - 1]:
        print(f'{m}.{n-1} {m+1}.01')
    elif n > number_of_days_in_a_month_of_the_year[m - 1]:
        print('Количество не должно превышать 31')
    else:
        print(f'{m}.{n-1} {m}.{n+1}')
elif 1 <= m <= 9:
    if m == 1 and n == 1:
        print('1 января в расчет не должно входить!')
        exit()
    if n == number_of_days_in_a_month_of_the_year[m - 1]:
        print(f'0{m}.{n-1} 0{m+1}.01')
    elif n > number_of_days_in_a_month_of_the_year[m - 1]:
        print('Количество не должно превышать 31')
    else:
        print(f'0{m}.{n-1} 0{m}.{n+1}')
else:
    print('Число месяца должно быть от 1 до 12')


