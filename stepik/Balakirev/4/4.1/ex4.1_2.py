word = input()
# print(word)
lower_word = word.lower()
print(lower_word)

if lower_word[:] == lower_word[::-1]:
    print(f"Слово {word} является словом полиндромом")
else:
    print(f"Слово {word} не является словом полиндромом")
