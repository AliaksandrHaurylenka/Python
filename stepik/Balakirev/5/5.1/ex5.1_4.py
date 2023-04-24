n = int(input())
i = 1

res = []
while i <= n:
    res.append(1 / i)
    i += 1

print(round(sum(res), 3))
