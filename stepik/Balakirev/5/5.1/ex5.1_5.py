x = int(input())

res = [x]
while x != 0:
    x = int(input())
    res.append(x)

print(sum(res))

