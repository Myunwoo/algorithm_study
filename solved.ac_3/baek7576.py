import sys
from collections import deque
input = sys.stdin.readline

M, N = list(map(int, input().split()))
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]


def bfs(graph, i, j):
  dq = deque()
  dq.append([i, j])
  dn = [1, -1, 0, 0]
  dm = [0, 0, 1, -1]

  while dq:
    curN, curM = dq.popleft()
    for k in range(4):
      newN = curN + dn[k]
      newM = curM + dm[k]
      if 0<=newN<N and 0<=newM<M and graph[newN][newM] == 0:
        graph[newN][newM] = graph[curN][curM]+1
        dq.append([newN, newM])

for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      bfs(graph, i, j)

done = True
m = -1
for i in range(N):
  for j in range(M):
    if graph[i][j] == 0:
      done = False
      break
    m = max(m, graph[i][j])
  if not done:
    break

if not done:
  print(-1)
else:
  print(m-1)