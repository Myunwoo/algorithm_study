import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(N)]

def bfs(i, j, target):
    global N, graph
    costs = [[float('inf') for _ in range(N)] for _ in range(N)]
    dq = deque()
    dn = [1, -1, 0, 0]
    dm = [0, 0, 1, -1]
    dq.append((i, j))
    costs[i][j] = 0
    totalCost = 0
    while dq:
        curN, curM = dq.popleft()
        curCost = costs[curN][curM]
        for i in range(4):
            newN = curN + dn[i]
            newM = curM + dm[i]
            if 0<=newN<N and 0<=newM<N and costs[newN][newM] > curCost + 1:
                dq.append((newN, newM))
                costs[newN][newM] = curCost + 1
                if graph[newN][newM] == target:
                    totalCost += costs[newN][newM]
                    if target == 2:
                        return totalCost
    return totalCost

chickens = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chickens.append((bfs(i, j, 1), i, j))

chickens.sort()
for _ in range(len(chickens)-M):
    cost, n, m = chickens.pop()
    graph[n][m] = 0

result = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result += bfs(i, j, 2)

print(result)