import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if dp[i][j] > 0 and graph[i][j] > 0:
            val = graph[i][j]
            if i+val < N:
                dp[i+val][j] += dp[i][j]
            if j+val < N:
                dp[i][j+val] += dp[i][j]

print(dp[-1][-1])