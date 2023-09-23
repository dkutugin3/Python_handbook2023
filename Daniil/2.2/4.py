name = ["Петя", "Вася", "Толя"]
result = []
for i in name:
    speed = int(input())
    result.append([speed, i])
result.sort(reverse=True)
for i in range(1, 4):
    print(f"{i}. {result[i - 1][1]}")
