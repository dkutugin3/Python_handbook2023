n = int(input())
count = 0
for i in range(n):
    now_str = input()
    if now_str == now_str[::-1]:
        count += 1
print(count)
