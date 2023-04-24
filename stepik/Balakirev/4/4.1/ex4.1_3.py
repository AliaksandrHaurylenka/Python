m, n = map(int, input().split())
# print(m, n)

if (m / n) == int(m / n):
    print(int(m / n))
else:
    print(f"{m} на {n} нацело не делится")
