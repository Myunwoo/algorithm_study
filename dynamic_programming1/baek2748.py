#https://www.acmicpc.net/problem/2748

dp=[-1 for _ in range(91)]
dp[0]=0
dp[1]=1
dp[2]=1
def fibo(x):
    if dp[x]!=-1:
        return dp[x]
    else:
        dp[x]=fibo(x-1)+fibo(x-2)
        return dp[x]
fibo(90)

n=int(input())
print(dp[n])