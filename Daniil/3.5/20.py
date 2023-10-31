ans = 0
with open("numbers.num", "rb") as f:
    while z := f.read(2):
        ans += int.from_bytes(z, "big", signed=False)
print(ans % 2 ** 16)
