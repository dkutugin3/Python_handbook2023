a = [i for i in range(1, 1001)]
while True:
    if len(a) % 2 == 0:
        number = len(a) // 2 - 1
    else:
        number = len(a) // 2
    k = a[number]
    print(k)
    if (inp := input()) == "Угадал!":
        exit()
    if inp == "Больше":
        a = a[number + 1:]
    else:
        a = a[:number]
