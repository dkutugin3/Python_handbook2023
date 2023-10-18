n_count = int(input())
m_count = int(input())
n = set()
m = set()
for i in range(n_count):
    n.add(input())

for i in range(m_count):
    m.add(input())

if len(m & n) != 0:
    print(len(m & n))
else:
    print("Таких нет")
