import sys
input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(graph, i, j, count):
  graph[i][j] = '0'
  for i in range(4):
    newI = i + dx[i]
    newJ = j + dy[i]
    if 0 <= newI < N and 0 <= newJ < N and graph[newI][newJ] == '1':
      dfs(graph, newI, newJ, count)
      count += 1
  return count

answer = []
for i in range(N):
  for j in range(N):
    if graph[i][j] == '1':
      answer.append(dfs(graph, i, j, 0))

print(answer)