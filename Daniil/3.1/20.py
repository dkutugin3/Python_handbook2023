from math import factorial

stack = []


def fact(n):
    return n[:-1] + [factorial(n[-1])]


def un_min(n):
    return n[:-1] + [-n[-1]]


def sharp(n):
    return n[:] + [n[-1]]


def dog(n):
    bf3 = n.pop(-1)
    bf2 = n.pop(-1)
    bf1 = n.pop(-1)
    return n + [bf2, bf3, bf1]


operation = {"!": fact, "~": un_min,
             "#": sharp, "@": dog}
string = input().replace("/", "//").split()
for s in string:
    if s.isnumeric():
        stack.append(int(s))
    elif s in operation.keys():
        stack = operation[s](stack)
    else:
        x2 = stack.pop(-1)
        x1 = stack.pop(-1)
        x3 = eval(f"{x1} {s} {x2}")
        stack.append(x3)
print(stack[0])
