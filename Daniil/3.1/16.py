L = int(input()) - 3
N = int(input())
result = []
for i in range(N):
    string = input()
    if len(string) < L:
        result.append(string)
        L -= len(string)
    else:
        result.append(string[:L] + "...")
        break
print(*result, sep="\n")
