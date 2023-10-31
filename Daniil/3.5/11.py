import json
from itertools import chain

data_file = input()
json_file = input()
with open(data_file, mode="r", encoding="utf-8") as file:
    data = list(chain.from_iterable([map(int, i.rstrip("\n").split()) for i in file]))
ans = {
    "count": len(data),
    "positive_count": len([i for i in data if i > 0]),
    "min": min(data),
    "max": max(data),
    "sum": sum(data),
    "average": round(sum(data) / len(data), 2)
}
with open(json_file, encoding="utf-8", mode="w") as file:
    json.dump(ans, file, ensure_ascii=False, indent=4)
