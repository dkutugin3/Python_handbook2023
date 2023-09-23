# p = 7  v = 6
# p = 6  v = 12
# p += n   v += m
p = 6
v = 12
p += int(input())
v += int(input())
if p > v:
    print("Петя")
else:
    print("Вася")