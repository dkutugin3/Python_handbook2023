name = input()
price = int(input())
weight = int(input())
money = int(input())
str2 = f"{weight}кг * {price}руб/кг"
print(f"""================Чек================
Товар:{name:>29}
Цена:{str2:>30}
Итого:{price * weight:>26}руб
Внесено:{money:>24}руб
Сдача:{money - price * weight:>26}руб
===================================""")

