#https://www.acmicpc.net/problem/2178

import sys
from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(sys.stdin.readline().strip()))
    for j in range(len(graph[i])):
        graph[i][j] = int(graph[i][j])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dq = deque()
costs = [[0 for _ in range(M)] for _ in range(N)]

def bfs():
    global dq
    global dx, dy
    dq.append([0,0])
    costs[0][0] = 1

    while dq:
        pos = dq.popleft()
        for i in range(4):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if costs[nx][ny] == 0:
                dq.append([nx,ny])
                costs[nx][ny] = costs[pos[0]][pos[1]] + 1 

bfs()
print(costs[N-1][M-1])