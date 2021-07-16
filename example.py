#https://www.acmicpc.net/problem/1753
import sys
from collections import deque

V, E = map(int, sys.stdin.readline().strip().split())
visited = [False for _ in range(V+1)]
graph = [[] for _ in range(V+1)]
costs = [sys.maxsize for _ in range(V+1)]

start = int(sys.stdin.readline().strip())

for _ in range(E):
    vertex = list(map(int, sys.stdin.readline().strip().split()))
    graph[vertex[0]].append([vertex[1],vertex[2]])

visited[start]=True
costs[start]=0
dq=deque()
dq.append([start,0])

while dq:
    node, cost = dq.popleft()
    for n in graph[now[0]]:
        if visited[n[0]] == False:
            visited[n[0]] = True
            costs[n[0]] = min(costs[n[0]],now[1]+n[1])
            dq.append(n)

for i in range(1,V+1):
    if costs[i] == sys.maxsize:
        print('INF')
    else:
        print(costs[i])