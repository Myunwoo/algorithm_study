import sys
input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = []
count = 0

def dfs(graph, i, j):
  graph[i][j] = '0'
  global count
  count += 1
  for k in range(4):
    newI = i + dx[k]
    newJ = j + dy[k]
    if 0 <= newI < N and 0 <= newJ < N and graph[newI][newJ] == '1':
      dfs(graph, newI, newJ)


for i in range(N):
  for j in range(N):
    if graph[i][j] == '1':
      count = 0
      dfs(graph, i, j)
      answer.append(count)

answer.sort()
print(len(answer))
for a in answer:
  print(a)