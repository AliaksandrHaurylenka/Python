n, m = map(int, input().split())

lst_odd = []
while n < m:
    lst_odd.append(n + 1)
    n += 2

print(*lst_odd)
