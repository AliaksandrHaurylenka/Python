n = int(input())

lst_Fibonacci = [1, 1]
i = 1
while i <= n - 2:
    lst_Fibonacci.append(lst_Fibonacci[i - 1] + lst_Fibonacci[i])
    i += 1

print(lst_Fibonacci)
