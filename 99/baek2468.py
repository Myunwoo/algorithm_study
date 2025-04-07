import sys
import copy
from collections import deque

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = 0
mn = 101
mx = -1
for i in range(N):
    for j in range(N):
        mn = min(mn, graph[i][j])
        mx = max(mx, graph[i][j])

# 모든 높이가 같아 최대 1개의 안전지대만 존재
if mn == mx:
    print(1)
    exit()

# startN, startM으로부터 시작하여 안전 지대를 모두 침수 지대로 만들고 리턴
def bfs(startN, startM, rain, newGprah):
    newGraph[startN][startM] = -1
    dq = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    dq.append([startN, startM])

    while dq:
        curN, curM = dq.popleft()
        for i in range(4):
            newN = curN + dx[i]
            newM = curM + dy[i]
            if 0 <= newN < N and 0 <= newM < N and newGraph[newN][newM] - rain > 0:
                newGraph[newN][newM] = -1
                dq.append([newN, newM])

for i in range(mn, mx):
    curResult = 0
    newGraph = copy.deepcopy(graph)
    for j in range(N):
        for k in range(N):
            if newGraph[j][k] - i > 0:
                curResult += 1
                bfs(j, k, i, newGraph)
    result = max(curResult, result)

print(result)