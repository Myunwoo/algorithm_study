#https://www.acmicpc.net/problem/2606

import sys
from collections import deque

n = int(sys.stdin.readline().strip())
v = int(sys.stdin.readline().strip())
visited = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(v):
    vertex = list(map(int, sys.stdin.readline().strip().split()))
    graph[vertex[0]].append(vertex[1])
    graph[vertex[1]].append(vertex[0])

def bfs():
    global graph, visited
    dq = deque()
    dq.append(1)
    count = 0
    visited[1] = True

    while dq:
        cur = dq.popleft()
        for node in graph[cur]:
            if visited[node] == False:
                dq.append(node)
                visited[node] = True
                count+=1
    
    return count

print(bfs())