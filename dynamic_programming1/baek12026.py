N = int(input())
arr = list(input())
dic = {
  'B': 'J',
  'O': 'B',
  'J': 'O'
}
dp = [float('inf') for _ in range(N)]
dp[0] = 0

for i in range(1, N):
  for j in range(i):
    if arr[j] == dic[arr[i]]:
      dp[i] = min(dp[i], dp[j]+(i-j)**2)

print(-1 if dp[-1] == float('inf') else dp[-1])