digits = map(int, input().split())
digits = [bin(i)[2:] for i in digits]
ans = []
for i in digits:
    buff_dict = dict()
    buff_dict["digits"] = len(i)
    buff_dict["units"] = i.count("1")
    buff_dict["zeros"] = i.count("0")
    ans.append(buff_dict)

print(ans)
