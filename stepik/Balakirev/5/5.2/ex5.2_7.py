n = int(input())

i = 1
num = []
while i <= n < 100:
    if i % 3 == 0 and i % 5 == 0:
        num.append(i)
        # i += 1

    i += 1
else:
    if n >= 100:
        print("слишком большое значение n")

print(*num)
