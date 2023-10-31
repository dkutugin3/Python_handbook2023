import os
from math import ceil

file_path = input()
size = os.path.getsize(file_path)
if size >= 1024 ** 3:
    print(f"{ceil(size / (1024 ** 3))}ГБ")
elif size >= 1024 ** 2:
    print(f"{ceil(size / (1024 ** 2))}МБ")
elif size >= 1024:
    print(f"{ceil(size / 1024)}КБ")
else:
    print(f"{size}Б")
