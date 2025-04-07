N, S, M = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[False for _ in range(M+1)] for _ in range(N+1)]
dp[0][S] = True

for i in range(1, N+1):
  volume = arr[i-1]
  for j in range(M+1):
    # 이전 볼륨
    if dp[i-1][j]:
      if j+volume <= M:
        dp[i][j+volume] = True
      if j-volume >= 0:
        dp[i][j-volume] = True

for i in range(M, -1, -1):
  if dp[N][i]:
    print(i)
    exit()

print(-1)