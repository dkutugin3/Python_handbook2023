final_set = set()
while s := input():
    lst = [""]
    lst.extend(s.split())
    lst.append("")
    for i in range(len(lst)):
        if lst[i] == "зайка":
            final_set.add(lst[i - 1])
            final_set.add(lst[i + 1])
final_set.discard("")
print(*final_set, sep="\n")
