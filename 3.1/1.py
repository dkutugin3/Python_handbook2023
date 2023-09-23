def check(a):
    rst = ["а", "б", "в"]
    if a in rst:
        return True
    return False


ms = [check(input()[0]) for i in range(int(input()))]
if all(ms):
    print('YES')
else:
    print("NO")
