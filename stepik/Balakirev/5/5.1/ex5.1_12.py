x = 100

lst = []
while x <= 999:
    if x % 47 == 43 and x % 3 == 0:
        lst.append(x)
    x += 1

print(lst)
