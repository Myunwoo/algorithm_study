import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(N)]
result = -1

one = [[0, 0], [0, 1], [0, 2], [1, 1]]
two = [[0, 0], [0, 1], [0, 2], [-1, 1]]
three = [[0, 0], [1, 0], [2, 0], [1, 1]]
four = [[0, 0], [1, 0], [2, 0], [1, -1]]

# ㅓ 모양을 제외하면, bfs로 풀이 가능
def bfs(N, M, n, m, graph):
    global result
    dn = [1, -1, 0, 0]
    dm = [0, 0, 1, -1]
    dq = deque()
    dq.append((n, m, 1, graph[n][m], [(n, m)]))
    m = -1
    while dq:
        curN, curM, curCount, curCost, curRoute = dq.popleft()
        for i in range(4):
            newN = curN + dn[i]
            newM = curM + dm[i]
            if 0<=newN<N and 0<=newM<M and curCount<4 and (newN, newM) not in curRoute:
                if curCount == 3:
                    result = max(result, curCost+graph[newN][newM])
                    continue
                dq.append((newN, newM, curCount+1, curCost+graph[newN][newM], curRoute+[(newN, newM)]))

# ㅓ 모양에 대한 cost
def checkOtherBlocks(N, M, n, m, graph, shapeArr):
    global result
    s = 0
    for shape in shapeArr:
        if not (0<=shape[0]+n<N and 0<=shape[1]+m<M):
            s = 0
            return
        s += graph[shape[0]+n][shape[1]+m]
    result = max(result, s)
    temp = list(map(lambda x:[x[0]+n, x[1]+m], shapeArr))

for i in range(N):
    for j in range(M):
        bfs(N, M, i, j, graph)
        checkOtherBlocks(N, M, i, j, graph, one)
        checkOtherBlocks(N, M, i, j, graph, two)
        checkOtherBlocks(N, M, i, j, graph, three)
        checkOtherBlocks(N, M, i, j, graph, four)

print(result)