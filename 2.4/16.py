def format_digit(a, length):
    return f"{a:^{length}}"


n = int(input())
now_length = int(input())
ryad = [format_digit(i * j, now_length) for i in range(1, n + 1) for j in range(1, n + 1)]
for i in range(0, n * n, n):
    buff = ryad[i:i + n]
    print(*buff, sep="|")
    if i != (n * n - n):
        print("-" * (n * now_length + n - 1))
