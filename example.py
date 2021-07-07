
import sys

V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    l = list(map(int,sys.stdin.readline().strip().split()))
    for i in range((len(l) // 2) - 1):
        graph[l[0]].append((l[i*2+1],l[i*2+2]))

visited = [False for _ in range(V+1)]

#dfs로 구한 지름을 리턴
def dfs(v):
    global visited
    visited[v] = True
    
    temp = []

    for vertex in graph[v]:
        if visited[vertex[0]] == True:
            continue
        temp.append(vertex[1] + dfs(vertex[0]))
    
    if temp:
        return max(temp)
    else:
        return -1

m = -1
for i in range(1, V+1):
    m = max(dfs(i), m)
    visited = [False for _ in range(V+1)]

print(m)