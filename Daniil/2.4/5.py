n = int(input())
count_all = 0
ans = 0
while count_all != n:
    f = 0
    while (inp := input()) != "ВСЁ":
        if inp == "зайка":
            f = 1
    count_all += 1
    ans += f
print(ans)
