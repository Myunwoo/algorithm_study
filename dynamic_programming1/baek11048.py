#https://www.acmicpc.net/problem/11048
import sys
N,M=map(int, sys.stdin.readline().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(1,N):
    graph[i][0]+=graph[i-1][0]
for i in range(1,M):
    graph[0][i]+=graph[0][i-1]

for i in range(1,N):
    for j in range(1,M):
        graph[i][j]+=max(graph[i-1][j],graph[i][j-1])

print(graph[N-1][M-1])