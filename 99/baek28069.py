import sys

N, K = map(int, input().split())
dp = [sys.maxsize for _ in range(N+1)]
dp[0] = 0

for i in range(N):
    if i+1 <= N:
        dp[i+1] = min(dp[i+1], dp[i]+1)
    if i+i//2 <= N:
        dp[i+i//2] = min(dp[i+i//2], dp[i]+1)

# 제자리 걸음에 의해 cost를 늘릴 수 있으므로, dp[N]<=K만 성립하면 이동이 가능한 것.
print('minigimbob' if dp[N]<=K else 'water')