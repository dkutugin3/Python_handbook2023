products = set()
for i in range(int(input())):
    products.add(input())

recipe = []
for i in range(int(input())):
    recipe_name = input()
    buff_set = set()
    for j in range(int(input())):
        buff_set.add(input())
    if buff_set <= products:
        recipe.append(recipe_name)

if recipe:
    print(*sorted(recipe), sep="\n")
else:
    print("Готовить нечего")
