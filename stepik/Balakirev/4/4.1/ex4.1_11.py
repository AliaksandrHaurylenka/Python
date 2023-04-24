t = float(input())

time_green = 3
time_red = 2

if 0 < t % (time_green + time_red) < time_green:
    print('green')
else:
    print("red")
