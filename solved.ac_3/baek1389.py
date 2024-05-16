import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().strip().split())
graph = [[float('inf') for _ in range(N)] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().strip().split())
    graph[A-1][B-1] = 1
    graph[B-1][A-1] = 1

# 각 사람을 거쳐가는 최단거리 갱신
for i in range(N):
    for j in range(N):
        for k in range(N):
            if j == k:
                graph[j][k]=0
            else:
              # j에서 k로 가는 길 = min(j에서 i를 거쳐 k로 가는 것, j에서 k로 가는 것)
              cost = min(graph[j][i]+graph[i][k], graph[j][k])
              graph[j][k] = cost
              graph[k][j] = cost

minCost = float('inf')
who = -1
for i in range(N):
    s = 0
    for j in range(len(graph[i])):
        if i == j:
            continue
        s += graph[i][j]
    if s < minCost:
        minCost = s
        who = i+1

print(who)