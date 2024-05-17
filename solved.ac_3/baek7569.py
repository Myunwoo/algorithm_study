from collections import deque
import sys
input = sys.stdin.readline

M, N, H = list(map(int, input().strip().split()))
graph = [[list(map(int, input().strip().split())) for _ in range(N)] for _ in range(H)]
dq = deque()
for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k] == 1:
        dq.append((i, j, k))

dh = [0, 0, 1, -1, 0, 0]
dn = [0, 0, 0, 0, 1, -1]
dm = [1, -1, 0, 0, 0, 0]

while dq:
  curH, curN, curM = dq.popleft()
  for i in range(6):
    newH = curH + dh[i]
    newN = curN + dn[i]
    newM = curM + dm[i]
    if 0<=newH<H and 0<=newN<N and 0<=newM<M and (graph[newH][newN][newM] == 0):
      graph[newH][newN][newM] = graph[curH][curN][curM]+1
      dq.append((newH, newN, newM))


m = -1
for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k] == 0:
        print(-1)
        exit()
      else:
        m = max(m, graph[i][j][k])

print(m-1)