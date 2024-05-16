import sys
from collections import deque
input = sys.stdin.readline

def bfs(N, M, n, m, graph):
    dq=deque()
    dn = [1, -1, 0, 0]
    dm = [0, 0, 1, -1]
    dq.append([n, m])
    graph[n][m] = 0

    while dq:
        curN, curM = dq.popleft()
        for i in range(4):
            newN = curN + dn[i]
            newM = curM + dm[i]
            if 0<=newN<N and 0<=newM<M and graph[newN][newM]==1:
                graph[newN][newM] = 0
                dq.append([newN, newM])

T = int(input())
for _ in range(T):
    count = 0
    M, N, K = map(int, input().strip().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().strip().split())
        graph[y][x] = 1
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(N, M, i, j, graph)
                count += 1
    
    print(count)