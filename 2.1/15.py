N = int(input())
M = int(input())
T = int(input())
time = N * 60 + M + T
print(f"{time // 60 % 24:0>2}:{time % 60:0>2}")
