#https://www.acmicpc.net/problem/1956
import sys
V,E=map(int, sys.stdin.readline().split())
graph=[[sys.maxsize for _ in range(V)] for _ in range(V)]
for _ in range(E):
    a,b,c,=map(int, sys.stdin.readline().split())
    graph[a-1][b-1]=c

for k in range(V):
    for i in range(V):
        for j in range(V):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])