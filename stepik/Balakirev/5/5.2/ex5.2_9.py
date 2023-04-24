x = int(input())

a = 10
i = 1
while True:
    if a < x:
        a *= 1.1
    else:
        break

    i += 1

print(i)
