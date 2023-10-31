from itertools import chain


def check_number(s: str):
    s = str(abs(int(s)))
    ans = 0
    for i in s:
        if int(i) % 2 == 0:
            ans += 1
        else:
            ans -= 1
    return ans


data_file = input()
even_file = input()
odd_file = input()
eq_file = input()
with open(data_file, mode="r", encoding="utf-8") as file:
    data = [i.rstrip("\n").split() for i in file]

ans_even = []
ans_odd = []
ans_eq = []
for i in data:
    buff_even = []
    buff_odd = []
    buff_eq = []
    for j in i:
        chk = check_number(j)
        if chk > 0:
            buff_even.append(j)
        elif chk == 0:
            buff_eq.append(j)
        else:
            buff_odd.append(j)
    ans_even.append(buff_even)
    ans_odd.append(buff_odd)
    ans_eq.append(buff_eq)

with open(even_file, encoding="utf-8", mode="w") as file:
    for i in ans_even:
        print(" ".join(i), file=file)
with open(odd_file, encoding="utf-8", mode="w") as file:
    for i in ans_odd:
        print(" ".join(i), file=file)
with open(eq_file, encoding="utf-8", mode="w") as file:
    for i in ans_eq:
        print(" ".join(i), file=file)
