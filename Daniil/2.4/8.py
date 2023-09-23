n = int(input())
name = ""
max_number = 0
for i in range(n):
    now_name = input()
    now_number = sum(map(int, list(input())))
    if now_number >= max_number:
        max_number = now_number
        name = now_name
print(name)
