k = 2
g = 1
for i in range(int(input())):
    g = 1 + i
    for j in range(g + k, 0, -1):
        print(f"До старта {j} секунд(ы)")
    print(f"Старт {g}!!!")
