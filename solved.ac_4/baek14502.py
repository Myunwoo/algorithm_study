from collections import deque
import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(N)]
result = -1

emptyArr = []
startArr = []
dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]

def bfs(graph):
  dq = deque()
  copyGraph = copy.deepcopy(graph)
  for start in startArr:
    dq.append(start)

  while dq:
    curN, curM = dq.popleft()
    for i in range(4):
      newN = curN + dn[i]
      newM = curM + dm[i]
      if 0<=newN<N and 0<=newM<M and copyGraph[newN][newM] == 0:
        copyGraph[newN][newM] = 2
        dq.append((newN, newM))
  count = 0
  for i in range(N):
    for j in range(M):
      if copyGraph[i][j] == 0:
        count += 1
  return count


for i in range(N):
  for j in range(M):
    if graph[i][j] == 0:
      emptyArr.append((i, j))
    elif graph[i][j] == 2:
      startArr.append((i, j))

for i in range(len(emptyArr)-2):
  for j in range(i+1, len(emptyArr)-1):
    for k in range(j+1, len(emptyArr)):
      one, two, three = emptyArr[i], emptyArr[j], emptyArr[k]
      graph[one[0]][one[1]] = 1
      graph[two[0]][two[1]] = 1
      graph[three[0]][three[1]] = 1
      result = max(result, bfs(graph))
      graph[one[0]][one[1]] = 0
      graph[two[0]][two[1]] = 0
      graph[three[0]][three[1]] = 0

print(result)