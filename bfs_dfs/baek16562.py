#https://www.acmicpc.net/problem/16562
import sys
from collections import deque

N,M,k=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
visited=[False for _ in range(N+1)]
costs=[0]+list(map(int, sys.stdin.readline().strip().split()))
for _ in range(M):
    a,b=map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(n):
    global graph,visited,costs
    dq=deque()
    dq.append(n)
    total_cost=sys.maxsize
    while dq:
        friend=dq.popleft()
        if visited[friend]:
            continue
        #방문처리
        visited[friend]=True
        #방문한 친구의 친구비 저장(최소값을 갱신할 때만)
        total_cost=min(costs[friend],total_cost)
        for i in graph[friend]:
            if not visited[i]:
                dq.append(i)   
    return total_cost

friend_costs=0
for i in range(1,N+1):
    if not visited[i]:
        friend_costs+=bfs(i)

if friend_costs <= k:
    print(friend_costs)
else:
    print('Oh no')