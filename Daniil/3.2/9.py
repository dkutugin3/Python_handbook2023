dict_count = {}
while n := input():
    n = n.split()
    for i in n:
        dict_count[i] = dict_count.get(i, 0)
        dict_count[i] += 1

for key, value in dict_count.items():
    print(key, value)
