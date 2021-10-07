#https://www.acmicpc.net/problem/2156
import sys
N=int(sys.stdin.readline())
grapes=[]
for _ in range(N):
    grapes.append(int(sys.stdin.readline()))

dp=[0 for _ in range(N)]
dp[0]=grapes[0]
dp[1]=grapes[0]+grapes[1]
if N==1:
    print(dp[N-1])
    exit()
dp[2]=max(dp[1],grapes[0]+grapes[2],grapes[1]+grapes[2])
if N==2:
    print(dp[N-1])
    exit()
for i in range(3,N):
        dp[i]=max(dp[i-3]+grapes[i-1]+grapes[i],dp[i-2]+grapes[i],dp[i-1])

print(dp[N-1])