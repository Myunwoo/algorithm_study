dp = [float('inf') for _ in range(1000001)]
X = int(input())

dp[1] = 0
for i in range(2, len(dp)):
  arr = []
  if i%3 == 0:
    arr.append(dp[i//3]+1)
  if i%2 == 0:
    arr.append(dp[i//2]+1)
  arr.append(dp[i-1]+1)
  dp[i] = min(arr)

print(dp[X])