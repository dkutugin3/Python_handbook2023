def format_string(s: str):
    s = s.replace("\t", "").replace("\n", "")
    buf = [i for i in s.split() if i]
    return " ".join(buf)


path1 = input()
path2 = input()
with open(path1, encoding="utf-8", mode="r") as read_file:
    with open(path2, encoding="utf-8", mode="w") as write_file:
        data = [format_string(i) for i in read_file if not i.isspace()]
        print(*data, sep="\n", file=write_file)
