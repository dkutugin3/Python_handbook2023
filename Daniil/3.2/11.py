n = int(input())
name_dict = dict()
ans = 0
for i in range(n):
    name = input()
    name_dict[name] = name_dict.get(name, 0)
    name_dict[name] += 1
print(sum([i[1] for i in name_dict.items() if i[1] != 1]))
