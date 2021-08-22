import sys
sys.setrecursionlimit(1000000000)

dp=[-1 for _ in range(100001)]
dp[0]=0
dp[1]=1

def fibo(n):
    if dp[n]!=-1:
        return dp[n]
    else:
        dp[n]=fibo(n-1)+fibo(n-2)
        return dp[n]

def solution(n):
    answer = 0
    fibo(100000)
    answer=dp[n]%1234567
    return answer