meet = dict()
while s := input():
    names = s.split()

    meet[names[0]] = meet.get(names[0], set())
    meet[names[0]].add(names[1])

    meet[names[1]] = meet.get(names[1], set())
    meet[names[1]].add(names[0])

all_names = sorted(meet.keys())
for i in all_names:
    private_set = set()
    for j in meet[i]:
        private_set = private_set | meet[j]
    private_set.discard(i)
    private_set = private_set - meet[i]
    print(f"{i}: ", end="")
    print(*sorted(private_set), sep=", ")
