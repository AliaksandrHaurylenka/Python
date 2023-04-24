slag = str(input())

a = slag.count('--')
# print(a)

while a != 0:
    slag = slag.replace('--', '-')
    a = slag.count('--')

print(slag)

# refsve--dfhndhdth---sdgss
