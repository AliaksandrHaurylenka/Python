summa = 0

while True:
    x = int(input())

    if x > 0:
        summa *= x
        print(summa)
    elif x == 0:
        break
    else:
        print(summa)
        continue
