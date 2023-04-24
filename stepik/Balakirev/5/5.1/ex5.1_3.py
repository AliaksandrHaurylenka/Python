x = float(input())
a = 2
b = 10

lst = []
while a <= 10:
    lst.append(round(x * a, 1))
    a += 1

print(*lst)
