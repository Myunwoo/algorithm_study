import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = [list(input().strip()) for _ in range(M)]

def bfs(i, j, color):
  global N, M, graph
  dq = deque()
  dm = [1, -1, 0, 0]
  dn = [0, 0, 1, -1]
  graph[i][j] = ''
  result = 1
  dq.append([i, j])
  while dq:
    curM, curN = dq.popleft()
    for i in range(4):
      newM = curM + dm[i]
      newN = curN + dn[i]
      if 0<=newM<M and 0<=newN<N and graph[newM][newN] == color:
        result += 1
        graph[newM][newN] = ''
        dq.append([newM, newN])
  return result**2

ws = 0
bs = 0
for i in range(M):
  for j in range(N):
    if graph[i][j] == 'W':
      ws += bfs(i, j, 'W')
    elif graph[i][j] == 'B':
      bs += bfs(i, j, 'B')

print(ws, bs)