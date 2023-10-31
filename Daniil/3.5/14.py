import json

data_path = input()
updates_path = input()
new_json = dict()
with open(data_path, "r", encoding="utf-8") as file:
    data = json.load(file)
for i in data:
    key = i.pop("name")
    new_json[key] = i

with open(updates_path, "r", encoding="utf-8") as file:
    data = json.load(file)
for i in data:
    key = i.pop("name")
    for j, k in i.items():
        new_json[key][j] = max(new_json[key].get(j, ""), k)

with open(data_path, "w", encoding="utf-8") as file:
    json.dump(new_json, file, ensure_ascii=False, indent=4)
