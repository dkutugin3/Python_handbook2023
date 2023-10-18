dct = {}
for i in range(int(input())):
    s = input().split()

    for i in range(1, len(s)):
        dct[s[i]] = dct.get(s[i], [])
        dct[s[i]].append(s[0])
key = input()
print(*sorted(dct.get(key, ["Таких нет"])), sep="\n")
