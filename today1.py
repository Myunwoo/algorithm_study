#https://www.acmicpc.net/problem/15724
import sys
N,M=map(int,sys.stdin.readline().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(N):
    for j in range(M-1):
        graph[i][j+1]+=graph[i][j]

for j in range(M):
    for i in range(N-1):
        graph[i+1][j]+=graph[i][j]

K=int(sys.stdin.readline())
for _ in range(K):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    result=graph[x2-1][y2-1]
    if x1-1>0:
        result-=graph[x1-2][y2-1]
    if y1-1>0:
        result-=graph[x2-1][y1-2]
    if x1-1>0 and y1-1>0:
        result+=graph[x1-2][y1-2]
    print(result)