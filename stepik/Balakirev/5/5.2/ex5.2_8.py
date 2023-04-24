n = int(input())

i = 1
# while i**2 < n:
#     i += 1
# else:
#     print(i)

while i <= n:
    if i**2 > n:
        print(i)
        break

    i += 1
