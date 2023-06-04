a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print('Равносторонний')
elif b == a != c or c == a != b or b == c != a:
    print("Равнобедренный")
elif b != a != c and b != c:
    print("Разносторонний")
