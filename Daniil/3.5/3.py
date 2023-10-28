from sys import stdin

ans = []
for i in stdin:
    i = i.rstrip("\n")
    if "#" in i:
        clear_data = i.split("#")[0]
        if clear_data:
            ans.append(clear_data)
    else:
        ans.append(i)
print(*ans, sep="\n")
