def solution():
    ans = {}
    max_val = 0
    let = ''
    while (inp := str(input())) != "ФИНИШ":
        inp = inp.lower()
        for letter in inp:
            if letter != ' ':
                ans[letter] = ans.get(letter, 0) + 1

    for i in sorted(ans.items()):
        if i[1] > max_val:
            max_val = i[1]
            let = i[0]
    print(let)


def main():
    solution()


if __name__ == "__main__":
    main()
