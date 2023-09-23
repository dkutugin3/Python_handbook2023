slovar = {'СЕВЕР': (0, 1), 'ЮГ': (0, -1), 'ЗАПАД': (-1, 0), 'ВОСТОК': (1, 0)}
coord = [0, 0]
while (s := input()) != "СТОП":
    k = int(input())
    coord = [coord[i] + slovar[s][i] * k for i in range(2)]
coord = coord[::-1]
print(*coord, sep="\n")
