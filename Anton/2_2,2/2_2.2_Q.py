def solution():
    a = float(input())
    b = float(input())
    c = float(input())
    D = b ** 2 - 4 * a * c
    if D < 0:
        sol1 = "No solution"
        sol2 = ''
    elif a == b and a == c and a == 0:
        sol1 = "Infinite solutions"
        sol2 = ''
    elif a == 0 and b == 0:
        sol1 = "No solution"
        sol2 = ''
    elif a == 0:
        sol1 = f"{-c / b:.2f}"
        sol2 = ''
    elif D == 0:
        sol1 = f"{-b / 2 * a:.2f}"
        sol2 = ''
    else:
        sol1 = (-b + D ** 0.5) / (2 * a)
        sol2 = (-b - D ** 0.5) / (2 * a)
        if sol1 > sol2:
            sol1, sol2 = sol2, sol1
        sol1 = f"{sol1:.2f}"
        sol2 = f" {sol2:.2f}"

    print(sol1 + sol2)


def main():
    solution()


if __name__ == "__main__":
    main()
