from sys import stdin

search_request = stdin.readline().rstrip("\n").lower()
files = [i.rstrip("\n") for i in stdin]
flag = 1
for f in files:
    with open(f, "r", encoding="utf-8") as file:
        data = file.read().replace("\n", " ").lower()
        while "  " in data:
            data = data.replace("  ", " ")
        if search_request in data:
            print(f)
            flag = 0
if flag:
    print("404. Not Found")
