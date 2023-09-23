name = ["Петя", "Вася", "Толя"]
lst = []
for i in range(3):
    lst.append([int(input()), name[i]])
lst.sort(reverse=True)
print(f"{lst[0][1]:^24}")
print(f"  {lst[1][1]:<22}")
print(f"{lst[2][1]:>22}  ")
print("   II      I      III   ")
