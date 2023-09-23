from math import factorial


def solution():
    stack = []
    inp = str(input()).split(" ")
    for elem in inp:
        try:
            stack.append(int(elem))
        except ValueError:
            if elem == '+':
                stack[-2] += stack[-1]
                del stack[-1]
            elif elem == '-':
                stack[-2] -= stack[-1]
                del stack[-1]
            elif elem == '*':
                stack[-2] *= stack[-1]
                del stack[-1]
            elif elem == '/':
                stack[-2] //= stack[-1]
                del stack[-1]
            elif elem == '~':
                stack[-1] = -stack[-1]
            elif elem == '!':
                stack[-1] = factorial(stack[-1])
            elif elem == '#':
                stack.append(stack[-1])
            elif elem == '@':
                stack.append(stack[-3])
                del stack[-4]

    print(stack[0])


def main():
    solution()


if __name__ == "__main__":
    main()
