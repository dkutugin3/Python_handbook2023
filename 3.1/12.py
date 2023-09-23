porridge = [
    "Манная",
    "Гречневая",
    "Пшённая",
    "Овсяная",
    "Рисовая"]
for i in range(int(input())):
    print(porridge[i % 5])

