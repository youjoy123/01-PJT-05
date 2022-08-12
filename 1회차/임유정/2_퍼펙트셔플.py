import sys

sys.stdin = open("_퍼펙트셔플.txt")

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())

    for _ in range(M):
        a, b = map(int, input().split())
        chy[a].append(b)
        chy[b].append(a)
    