stack = []
string = input().split()
for s in string:
    if s.isnumeric():
        stack.append(int(s))
    else:
        x2 = stack.pop(-1)
        x1 = stack.pop(-1)
        x3 = eval(f"{x1} {s} {x2}")
        stack.append(x3)
print(stack[0])
