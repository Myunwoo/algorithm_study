#https://www.acmicpc.net/problem/10942
import sys
N=int(sys.stdin.readline())
nums=list(map(int, sys.stdin.readline().strip().split()))

#길이가 1인 경우는 팰린드롬 이므로 1저장
dp=[[-1 for _ in range(N)] for _ in range(N)]
for i in range(N):
    dp[i][i]=1

#길이가 2인 경우는 두 수가 같다면 팰린드롬
for i in range(N-1):
    if nums[i]==nums[i+1]:
        dp[i][i+1]=1
        dp[i+1][i]=1
    else:
        dp[i][i+1]=0
        dp[i+1][i]=0

#길이가 3이상인 경우는 dp[start][end],dp[start+1][end-1]순으로 nums를 확인
#길이가 3인 것부터 N인 것까지
for length in range(2,N):
    #dp[start+1][end-1]가 팰린드롬인지 검사
    for i in range(N-length):
        if nums[i]==nums[i+length] and dp[i+1][i+length-1]==1:
            dp[i][i+length]=1
            dp[i+length][i]=1
        else:
            dp[i][i+length]=0
            dp[i+length][i]=0

M=int(sys.stdin.readline())
results=[]
for _ in range(M):
    start,end=map(int, sys.stdin.readline().split())
    results.append(dp[start-1][end-1])

for r in results:
    print(r)