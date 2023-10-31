import json
from sys import stdin

with open("scoring.json", "r", encoding="utf-8") as file:
    data = json.load(file)

answers = [i.rstrip("\n") for i in stdin]
output = 0
for test_dict in data:
    corr_ans = 0
    for test in test_dict["tests"]:
        if test["pattern"] == answers.pop(0):
            corr_ans += 1
    output += test_dict["points"] // len(test_dict["tests"]) * corr_ans
print(output)
