import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
items = [list(map(int, input().strip().split())) for _ in range(N)]
dp = [0 for _ in range(K+1)]

items.sort()

for i in range(N):
    dp[items[i][0]] = max(dp[items[i][0]], items[i][1])
    for j in range(i+1, N):
        if items[i][0]+items[j][0] <= K:
            dp[items[i][0]+items[j][0]] = max(dp[items[i][0]+items[j][0]], dp[items[i][0]] + items[j][1])
        else:
            continue

print(max(dp))