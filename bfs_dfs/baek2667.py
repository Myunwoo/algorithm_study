#https://www.acmicpc.net/problem/2667

import sys

N = int(input())
graph = []
for i in range(N):
    line = list(sys.stdin.readline().strip())
    graph.append(line)
    for j in range(N):
        graph[i][j] = int(graph[i][j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
blocks = 0

def dfs(x, y):
    global dx
    global dy
    global graph
    global blocks
    graph[x][y] = 0
    blocks += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if graph[nx][ny] == 1:
            dfs(nx,ny)

results = []
count = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i,j)
            results.append(blocks)
            count += 1
            blocks = 0

print(count)
results.sort()
for r in results:
    print(r)