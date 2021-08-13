#https://www.acmicpc.net/problem/11726
import sys
sys.setrecursionlimit(10000)
n=int(input())

dp=[-1 for _ in range(1001)]
dp[0]=0
dp[1]=1
dp[2]=2

def tile(x):
    if dp[x]!=-1:
        return dp[x]
    else:
        dp[x]=tile(x-1)+tile(x-2)
        return dp[x]

tile(1000)
print(dp[n]%10007)