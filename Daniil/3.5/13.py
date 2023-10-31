from sys import stdin
import json

name_file = input()
with open(name_file, "r", encoding="utf-8") as file:
    ans = json.load(file)

for i in stdin:
    key, value = i.rstrip("\n").replace(" ", "").split("==")
    ans[key] = value
with open(name_file, "w", encoding="utf-8") as file:
    json.dump(ans, file, ensure_ascii=False, indent=4)
