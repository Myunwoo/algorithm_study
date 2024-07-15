import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(N)]
costs = [[sys.maxsize for _ in range(M)] for _ in range(N)]

def bfs(startPoints):
    dn = [1, 1, 1, 0, -1, -1, -1, 0]
    dm = [1, 0, -1, -1, -1, 0, 1, 1]
    dq = deque()
    for s in startPoints:
        dq.append(s)
    while dq:
        curN, curM = dq.popleft()
        curCost = costs[curN][curM]
        for i in range(8):
            newN = curN + dn[i]
            newM = curM + dm[i]
            if 0<=newN<N and 0<=newM<M and costs[newN][newM] > curCost+1:
                costs[newN][newM] = curCost+1
                dq.append([newN, newM])


startPoints = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            startPoints.append([i, j])
            costs[i][j] = 0
bfs(startPoints)

answer = -1
for i in range(N):
    for j in range(M):
        answer = max(answer, costs[i][j])
print(answer)