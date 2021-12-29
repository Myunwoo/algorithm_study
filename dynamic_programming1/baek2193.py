#https://www.acmicpc.net/problem/2193
N=int(input())
dp=[[0,0] for _ in range(91)]
dp[1][0]=0
dp[1][1]=1
dp[2][0]=1
dp[2][1]=0

for i in range(3,91):
    dp[i][0]=dp[i-1][0]+dp[i-2][0]
    dp[i][1]=dp[i-1][1]+dp[i-2][1]

print(dp[N][0]+dp[N][1])