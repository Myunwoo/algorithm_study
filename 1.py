#https://www.acmicpc.net/problem/1516
import sys
from collections import deque
N=int(sys.stdin.readline())
dp=[0 for _ in range(N+1)]
time=[0 for _ in range(N+1)]
degree=[0 for _ in range(N+1)]
graph=[[] for _ in range(N+1)]

for i in range(N):
    arr=list(map(int,sys.stdin.readline().strip().split()))
    time[i+1]+=arr[0]
    
    #맨 끝은 -1이니까 제외
    for j in range(1,len(arr)-1):
        graph[arr[j]].append(i+1)
        degree[i+1]+=1

dq=deque()
#진입차수가 처음부터 0인 것을 dq에 삽입하면서 dp에 시간 저장
for i in range(1,N+1):
    if degree[i]==0:
        dq.append(i)
        dp[i]=time[i]

while dq:
    #진입차수가 0인 것 제거
    n=dq.popleft()
    #연결된 노드들 진입차수 내리기
    for g in graph[n]:
        degree[g]-=1
        #g건물을 짓는 시간은 g건물짓는시간+n건물 짓는시간이다.
        #대신! g건물을 짓는 시간을 사전에 계산했다면 비교해 주어야 함.
        #dp[g]=time[g]+dp[n]
        dp[g]=max(dp[g],time[g]+dp[n])
        #진입차수가 0이 되는 것은 dq에 삽입
        if degree[g]==0:
            dq.append(g)

for i in range(1,N+1):
    print(dp[i])