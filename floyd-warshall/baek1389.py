#https://www.acmicpc.net/problem/1389
import sys
N,M=map(int, sys.stdin.readline().split())
graph=[[sys.maxsize for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j:
                graph[i][j]=0
            else:
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

m=sys.maxsize
result=0
for i in range(N):
    if sum(graph[i])<m:
        m=sum(graph[i])
        result=i+1
print(result)