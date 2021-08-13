#https://www.acmicpc.net/problem/1149
import sys
N=int(sys.stdin.readline())
dp=[0,0,0]
houses=[]
for _ in range(N):
    houses.append(list(map(int, sys.stdin.readline().strip().split())))

dp[0],dp[1],dp[2]=houses[0][0],houses[0][1],houses[0][2]

for i in range(1,N):
    pre_r,pre_g,pre_b = dp[0],dp[1],dp[2]
    cur_r,cur_g,cur_b=houses[i][0],houses[i][1],houses[i][2]
    
    dp[0]=min(cur_r+pre_g,cur_r+pre_b)
    dp[1]=min(cur_g+pre_r,cur_g+pre_b)
    dp[2]=min(cur_b+pre_r,cur_b+pre_g)

print(min(dp))