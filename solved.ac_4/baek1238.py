import sys
input = sys.stdin.readline
from collections import deque

N, M, X = map(int, input().strip().split())
graph = [[float('inf') for _ in range(N)] for _ in range(N)]

for _ in range(M):
    start, end, time = map(int, input().strip().split())
    graph[start-1][end-1] = time

def dijkstra(s):
    tempGraph = [[float('inf') for _ in range(N)] for _ in range(N)]
    dq = deque()
    dq.append(s-1)
    tempGraph[s-1][s-1] = 0
    while dq:
        cur = dq.popleft()
        curCost = temp
        for i in range(len(graph[i])):
            if graph[i] != float('inf'):
