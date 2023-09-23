count = 0
while (a := input()) != "Приехали!":
    if "зайка" in a:
        count += 1
print(count)