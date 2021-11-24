#https://www.acmicpc.net/problem/15730
import sys
from collections import deque

N,M=map(int, sys.stdin.readline().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

rains=[[0 for _ in range(M)] for _ in range(N)]
result=0

for i in range(1,N-1):
    for j in range(1,M-1):
        leftMax=max(graph[i][:j])
        rightMax=max(graph[i][j+1:])
        topMax=0
        botMax=0
        for t in range(0,i):
            if graph[t][j]>topMax:
                topMax=graph[t][j]
        for t in range(i+1,N):
            if graph[t][j]>botMax:
                botMax=graph[t][j]

        m=min(leftMax,rightMax,topMax,botMax)
        if m>graph[i][j]:
            rains[i][j]=m-graph[i][j]

for r in rains:
    result+=sum(r)

print(result)