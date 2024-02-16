import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
visited = [False for _ in range(N)]
graph = [[False for _ in range(N)] for _ in range(N)]
for _ in range(M):
  a, b = list(map(int, input().split()))
  graph[a-1][b-1] = True
  graph[b-1][a-1] = True

dq = deque()
dq.append(0)
visited[0] = True

while dq:
  cur = dq.popleft()
  for i,v in enumerate(graph[cur]):
    if v and not visited[i]:
      visited[i] = True
      dq.append(i)

answer = -1
for v in visited:
  if v:
    answer += 1
print(answer)