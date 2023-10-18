map_dict = dict()
for i in range(int(input())):
    x, y = map(int, input().split())
    x = x - x % 10
    y = y - y % 10
    map_dict[(x, y)] = map_dict.get((x, y), 0)
    map_dict[(x, y)] += 1
print(max(map_dict.values()))
