a = [int(input()) for i in range(int(input()))]
degree = int(input())


def solution(n):
    return n ** degree


print(*list(map(solution, a)), sep="\n")
