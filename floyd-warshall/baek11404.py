#https://www.acmicpc.net/problem/11404
import sys
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
graph=[[sys.maxsize for _ in range(N)] for _ in range(N)]
for _ in range(M):
    A,B,C=map(int, sys.stdin.readline().split())
    graph[A-1][B-1]=min(graph[A-1][B-1],C)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j:
                graph[i][j]=0
            else:
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(len(graph)):
    for s in graph[i]:
        if s==sys.maxsize:
            print(0, end=' ')
        else:
            print(s,end=' ')
    print()