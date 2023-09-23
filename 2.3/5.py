total = 0
while True:
    if (price := float(input())) != 0:
        total += price if price < 500 else price * 0.9
    else:
        print(total)
        exit()
