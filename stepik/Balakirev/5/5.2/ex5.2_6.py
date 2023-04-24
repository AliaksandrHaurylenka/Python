lst_students = list(map(str, input().split()))

i = 0
msg = "НЕТ"
while i < len(lst_students):
    name_lower = lst_students[i].lower()

    if name_lower[0:1] == name_lower[-1:]:
        msg = "ДА"
        break
    else:
        i += 1

# Петр Анна Иван Сергей Михаил Федор
print(msg)
