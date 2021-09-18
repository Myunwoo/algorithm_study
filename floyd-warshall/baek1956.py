#https://www.acmicpc.net/problem/1956
import sys
V,E=map(int, sys.stdin.readline().split())
graph=[[sys.maxsize for _ in range(V)] for _ in range(V)]
for _ in range(E):
    a,b,c,=map(int, sys.stdin.readline().split())
    graph[a-1][b-1]=c

#i에서 시작해서 j로 가는 최소비용을 구하는 알고리즘. i시작,i도착의 경우를 0으로 처리하지 않으면, 싸이클이 존재하는 경우에도 싸이클을 고려한 값이 나온다.
m=sys.maxsize
for k in range(V):
    for i in range(V):
        for j in range(V):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
                if i==j:
                    if m>graph[i][j]:
                        m=graph[i][j]

if m==sys.maxsize:
    print(-1)
else:
    print(m)