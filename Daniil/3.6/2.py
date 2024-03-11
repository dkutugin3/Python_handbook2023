ans_dict = dict()
while (s := input()) != "":
    s = s.lower().split()
    for word in s:
        ans_dict[word[-1].capitalize()] = ans_dict.get(word[-1].capitalize(), set())
        ans_dict[word[-1].capitalize()].add(word)

for key, item in ans_dict.items():
    print(f"{key} - ", end="")
    print(*sorted(item), sep=", ")
