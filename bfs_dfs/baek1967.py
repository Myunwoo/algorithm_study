#https://www.acmicpc.net/problem/1967

import sys
from collections import deque

n = int(sys.stdin.readline().strip())

dq = deque()
costs = [-1 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child, cost = map(int,sys.stdin.readline().strip().split())
    graph[parent].append([child,cost])
    graph[child].append([parent,cost])

def bfs(start):
    global graph
    global dq
    global costs
    dq.append(start)
    costs[start] = 0
    
    while dq:
        pos = dq.popleft()
        for n in graph[pos]:
            if costs[n[0]] == -1:
                dq.append(n[0])
                costs[n[0]] = n[1] + costs[pos]

bfs(1)
new = costs.index(max(costs))
        
dq.clear()
costs = [-1 for _ in range(n+1)]



bfs(new)
print(max(costs))