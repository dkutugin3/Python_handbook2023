n = int(input())
buffer = []
for i in range(n):
    buffer.append(input())
search = input().lower()
result = [buffer[i] for i in range(n) if search in buffer[i].lower()]
print(*result, sep="\n")
