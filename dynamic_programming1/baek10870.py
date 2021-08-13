#https://www.acmicpc.net/problem/10870
dp=[-1 for _ in range(21)]
n=int(input())
dp[0]=0
dp[1]=1

def fibo(x):
    if dp[x]!=-1:
        return dp[x]
    else:
        dp[x]=fibo(x-1)+fibo(x-2)
        return dp[x]
fibo(20)
print(dp[n])