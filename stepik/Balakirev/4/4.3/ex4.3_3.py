word = str(input()).lower()

msg = 'палиндром' if word == word[::-1] else "не палиндром"
print(msg)
