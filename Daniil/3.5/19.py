shift = int(input())


def shift_symbol(char):
    cap = char.isupper()
    char = char.lower()
    if char.isalpha():
        ans = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
    else:
        return char
    if cap:
        return ans.upper()
    return ans


with open("public.txt", "r", encoding="utf-8") as file:
    arr = map(shift_symbol, list(file.read()))
    with open("private.txt", "w", encoding="utf-8") as w_file:
        w_file.write("".join(arr))
