#https://www.acmicpc.net/problem/2842

from collections import deque

N = int(input())
graph = []
costs = []
results = []

for _ in range(N):
    graph.append(list(input()))
for _ in range(N):
    costs.append(list(map(int,input().split())))

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'P':
            bfs(i,j)

def bfs(x, y):
    global graph, costs, results
    global dx, dy
    