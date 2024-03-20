from collections import deque
import sys
input = sys.stdin.readline

M, N, H = list(map(int, input().strip().split()))
graph = [[list(map(int, input().strip().split())) for _ in range(N)] for _ in range(H)]
cost = [[float('inf') for _ in range(M)] for _ in range(N) for _ in range(H)]

dh = [0, 0, 1, -1, 0, 0]
dn = [0, 0, 0, 0, 1, -1]
dm = [1, -1, 0, 0, 0, 0]

def bfs(graph, cost, h, n, m):
  print(h, n, m)
  cost[h][n][m] = 0
  dq = deque()
  dq.append((h, n, m))
  while dq:
    curH, curN, curM = dq.popleft()
    for i in range(6):
      newH = curH + dh[i]
      newN = curN + dn[i]
      newM = curM + dm[i]
      if 0<=newH<H and 0<=newN<N and 0<=newM<M and (cost[newH][newN][newM] > cost[curH][curN][curM]+1):
        cost[newH][newN][newM] = cost[curH][curN][curM]+1
        dq.append((newH, newN, newM))


for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k] == 1:
        bfs(graph, cost, i, j, k)