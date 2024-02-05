from collections import deque

N, M, V = list(map(int, input().split()))
graph = [[False for _ in range(N)] for _ in range(N)]
dfsVisited = [False for _ in range(N)]
bfsVisited = [False for _ in range(N)]
dfsAnswer = []
bfsAnswer = []
for _ in range(M):
  x, y = list(map(int, input().split()))
  graph[x-1][y-1] = True
  graph[y-1][x-1] = True

def dfs(graph, V, dfsAnswer):
  for i, g in enumerate(graph[V]):
    if g == True and not dfsVisited[i]:
      dfsVisited[i] = True
      dfsAnswer.append(i+1)
      dfs(graph, i, dfsAnswer)
    

dfsAnswer.append(V)
dfsVisited[V-1] = True
dfs(graph, V-1, dfsAnswer)

def bfs(graph, V, bfsVisited):
  dq = deque()
  dq.append(V)
  while dq:
    cur = dq.popleft()
    for i, g in enumerate(graph[cur]):
      if g == True and not bfsVisited[i]:
        dq.append(i)
        bfsVisited[i] = True
        bfsAnswer.append(i+1)
        

bfsAnswer.append(V)
bfsVisited[V-1] = True
bfs(graph, V-1, bfsVisited)

for i in range(len(dfsAnswer)):
  if i < N-1:
    print(dfsAnswer[i], end=' ')
  else:
    print(dfsAnswer[i])
for i in range(len(bfsAnswer)):
  if i < N-1:
    print(bfsAnswer[i], end=' ')
  else:
    print(bfsAnswer[i])