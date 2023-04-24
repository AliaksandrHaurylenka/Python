n = int(input())

i = 1
lst_contribution = [1000]
while i <= n:
    lst_contribution.append(lst_contribution[i - 1] * 1.05)
    i += 1

print(round(lst_contribution[-1], 2))
