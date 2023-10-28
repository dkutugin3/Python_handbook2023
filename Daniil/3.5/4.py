from sys import stdin

data = [i.rstrip("\n") for i in stdin]
request = data.pop(-1).lower()
for i in data:
    if request in i.lower():
        print(i)
