#https://www.acmicpc.net/problem/2623
import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
degree=[0 for _ in range(N+1)]

#위상정렬의 공식! 진입차수 설정
for _ in range(M):
    teams=list(map(int,sys.stdin.readline().strip().split()))
    for i in range(1,len(teams)-1):
        degree[teams[i+1]]+=1
        graph[teams[i]].append(teams[i+1])

dq=deque()
result=[]
#진입차수가 0인 경우 삽입
for i in range(1,len(degree)):
    if degree[i]==0:
        dq.append(i)

while dq:
    team=dq.popleft()
    for t in graph[team]:
        degree[t]-=1
        if degree[t]==0:
            dq.append(t)
    result.append(team)

#위상정렬이 불가능한 경우-> 어딘가에 순환이 있음->
#조건이 되는 노드를 모두 방문해도 진입 차수가 0인 노드가 존재하지 않게됨-> 모든 노드 방문 못하고 정렬이 끝나버림
if len(result)!=N:
    print(0)
else:
    for r in result:
        print(r)