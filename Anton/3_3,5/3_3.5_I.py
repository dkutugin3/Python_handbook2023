from itertools import chain
from sys import stdin


def solution():
    with open(input(), "r", encoding="UTF-8") as file:
        with open(input(), "w", encoding="UTF-8") as ans:
            for line in file.readlines():
                line = line.strip(" \t\n")
                line = line.replace('\t', '')
                line = ' '.join([word for word in line.split(' ') if word != '']) + '\n'
                if line != '\n':
                    ans.write(line)


def main():
    solution()


if __name__ == "__main__":
    main()
