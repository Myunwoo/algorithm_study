#https://www.acmicpc.net/problem/11403
import sys
N=int(sys.stdin.readline())
graph=[]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k]==1 and graph[k][j]==1:
                graph[i][j]=1

for g in graph:
    for t in g:
        print(t, end=' ')
    print()