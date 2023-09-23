n = int(input())
if n % 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print("YES")
            exit()
        else:
            print("NO")
            exit()
    print("YES")

else:
    print("NO")

