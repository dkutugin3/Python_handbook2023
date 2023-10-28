from itertools import chain

a = list(chain(*(input().replace(",", "").split() for i in range(3))))
for i, j in enumerate(sorted(a), 1):
    print(f"{i}. {j}")

# a = [i for j in range(3) for i in input().replace(",", "").split()]
# for i, j in enumerate(sorted(a),1):
#     print(f"{i}. {j}")
