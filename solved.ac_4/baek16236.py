import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [list(map(int, input().strip().split())) for _ in range(N)]
eat = 0
curSize = 2
fishDic = {}
totalCount = 0

def bfs(i, j):
    global eat, curSize, graph, N, fishDic
    graph[i][j] = 0
    costs = [[10000 for _ in range(N)] for _ in range(N)]
    dn = [-1, 0, 1, 0]
    dm = [0, -1, 0, 1]
    dq = deque()
    dq.append([i, j])
    costs[i][j] = 0

    while dq:
        curN, curM = dq.popleft()
        curCost = costs[curN][curM]
        for i in range(4):
            newN = curN + dn[i]
            newM = curM + dm[i]
            if 0<=newN<N and 0<=newM<N and graph[newN][newM] <= curSize and costs[newN][newM] > curCost+1:
                costs[newN][newM] = curCost + 1
                dq.append([newN, newM])
                if (newN, newM) in fishDic and graph[newN][newM] < curSize:
                    fishDic[(newN, newM)] = costs[newN][newM]

# 먹을 수 있는 물고기 중, 거리가 가장 가까운 물고기, 여러 마리라면 가장 위에 있는 물고기, 여러 마리라면 가장 왼쪽에 있는 물고기
for i in range(N):
    for j in range(N):
        if graph[i][j] > 0 and graph[i][j] != 9:
            fishDic[(i, j)] = float('inf')

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            bfs(i, j)

while len(list(fishDic.keys())) > 0:
    keys = list(fishDic.keys())
    keys.sort()
    minVal = float('inf')
    minN, minM = 0, 0
    for k in keys:
        if fishDic[k] < minVal:
            minVal = fishDic[k]
            minN, minM = k[0], k[1]
            
    if minVal < float('inf'):
        eat += 1
        if eat == curSize:
            curSize += 1
            eat = 0
        totalCount += fishDic[(minN, minM)]
        del fishDic[(minN, minM)]
        bfs(minN, minM)
    else:
        break

print(totalCount)