import sys
input = sys.stdin.readline
N, K = map(int, input().strip().split())
words = [input().strip() for _ in range(N)]

if K < 5:
    print(0)
    exit()

