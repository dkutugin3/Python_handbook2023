from itertools import chain
from sys import stdin


def solution():
    with open(input(), "r", encoding="UTF-8") as file:
        with open(input(), "w", encoding="UTF-8") as even:
            with open(input(), "w", encoding="UTF-8") as odd:
                with open(input(), "w", encoding="UTF-8") as eq:
                    for line in file.readlines():
                        nums = line.rstrip(" \n").split(" ")
                        evens = []
                        odds = []
                        eqs = []
                        for num in nums:
                            stat = num.replace("3", "1").replace("5", "1").replace("7", "1").replace("9", "1")
                            stat = stat.replace("2", "0").replace("4", "0").replace("6", "0").replace("8", "0")
                            stat = (stat.count("0"), stat.count("1"))
                            if stat[0] > stat[1]:
                                evens.append(num)
                            elif stat[0] < stat[1]:
                                odds.append(num)
                            else:
                                eqs.append(num)

                        even.write(" ".join(evens) + "\n")
                        odd.write(" ".join(odds) + "\n")
                        eq.write(" ".join(eqs) + "\n")


def main():
    solution()


if __name__ == "__main__":
    main()
