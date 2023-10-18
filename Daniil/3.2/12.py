n = int(input())
name_dict = dict()
ans = 0
for i in range(n):
    name = input()
    name_dict[name] = name_dict.get(name, 0)
    name_dict[name] += 1

name_list = sorted([[i, name_dict[i]] for i in name_dict])
flag = 1
for name, count in name_list:
    if count != 1:
        print(f"{name} - {count}")
        flag = 0
if flag:
    print("Однофамильцев нет")
