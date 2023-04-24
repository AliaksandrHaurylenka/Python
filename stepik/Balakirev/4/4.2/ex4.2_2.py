a, b, c = map(int, input().split())
# print(a, b, c)

# 8 11 -1
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)
