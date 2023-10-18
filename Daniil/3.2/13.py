menu = set()
for i in range(int(input())):
    menu.add(input())

ex_eat = set()
for i in range(int(input())):
    for j in range(int(input())):
        ex_eat.add(input())

if menu - ex_eat:
    print(*sorted(menu - ex_eat), sep="\n")
else:
    print("Готовить нечего")
