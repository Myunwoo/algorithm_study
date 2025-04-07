import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    dp[i] = max(dp[i-1], dp[i])
    time, val = arr[i-1]
    if i+time-1 > N:
        continue
    dp[i+time-1] = max(dp[i+time-1], dp[i-1]+val)

print(max(dp))