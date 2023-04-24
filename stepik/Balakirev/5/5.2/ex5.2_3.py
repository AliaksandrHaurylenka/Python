p = [0] * 10
# print(p)
# print(len(p))

i = 1
while i < len(p) and p.count(1) != 5:
    # if p.count(1) == 5:
    #     break
    i += 1
    x = int(input())

    if p[x] == 0:
        p[x] = 1
    else:
        continue

    print(p)
    # i += 1

print(*p)
