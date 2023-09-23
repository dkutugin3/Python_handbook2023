result = []
for i in range(int(input())):
    string = input()
    if string.find("зайка") == -1:
        result.append("Заек нет =(")
    else:
        result.append(string.find("зайка") + 1)
print(*result, sep="\n")
