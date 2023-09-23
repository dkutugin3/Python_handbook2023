a = float(input())
b = float(input())
c = float(input())
if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
    exit()
if a == 0 and b == 0:
    print("No solution")
    exit()
if a == 0:
    print(f"{-c / b:.2f}")
    exit()
d = b ** 2 - 4 * a * c
if d < 0:
    print("No solution")
    exit()
if d == 0:
    print(f"{-b / (2 * a):.2f}")
    exit()
res = [(-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)]
res.sort()
print(f"{res[0]:.2f} {res[1]:.2f}")
