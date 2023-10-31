def transform_char(s: str):
    return chr(ord(s) % 128)


with open("secret.txt", "r", encoding="utf-8") as file:
    ans = "".join(map(transform_char, list(file.read())))
    print(ans)
