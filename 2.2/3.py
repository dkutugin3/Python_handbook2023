name = ["Петя", "Вася", "Толя"]
result = []
for i in name:
    speed = int(input())
    result.append([speed, i])
result.sort(reverse=True)
print(result[0][1])
