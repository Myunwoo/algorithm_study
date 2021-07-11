#https://www.acmicpc.net/problem/11724

import sys

N, M = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

def dfs(start):
    global graph
    global visited
    visited[start] = True
    for node in graph[start]:
        if visited[node] == False:
            dfs(node)
    

count = 0

for i in range(1, N+1):
    if visited[i] == False:
        dfs(i)
        count += 1

print(count)