a = [i if int(i) % 2 != 0 else "" for i in input()]
print(*a, sep='')
