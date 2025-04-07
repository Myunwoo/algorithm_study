T = int(input())
dp = [0 for _ in range(10001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 10001):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    print(dp[int(input())])
