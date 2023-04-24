n = int(input())

i = 3
lst_cells = [1]
while i <= n:
    if i % 3 == 0:
        lst_cells.append(lst_cells[-1] * 2)

    i += 1

print(lst_cells[-1])
