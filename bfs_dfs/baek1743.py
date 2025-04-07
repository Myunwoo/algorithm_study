import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
graph = [['.' for _ in range(M)] for _ in range(N)]
dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]

for _ in range(K):
  n, m = map(int, input().strip().split())
  graph[n-1][m-1] = '#'

def bfs(i, j):
  global graph, N, M, dn, dm
  result = 1
  graph[i][j] = '.'
  dq = deque()
  dq.append([i, j])
  while dq:
    curN, curM = dq.popleft()
    for i in range(4):
      newN = curN + dn[i]
      newM = curM + dm[i]
      if 0<=newN<N and 0<=newM<M and graph[newN][newM]=='#':
        graph[newN][newM] = '.'
        dq.append([newN, newM])
        result += 1
  return result

answer = 0
for i in range(N):
  for j in range(M):
    if graph[i][j] == '#':
      answer = max(answer, bfs(i, j))
print(answer)