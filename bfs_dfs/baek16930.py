import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
graph = [list(input().strip()) for _ in range(N)]
costs = [[sys.maxsize for _ in range(M)] for _ in range(N)]
startN, startM, endN, endM = map(int, input().strip().split())
costs[startN-1][startM-1] = 0

def bfs():
    global costs
    dn = [1, -1, 0, 0]
    dm = [0, 0, 1, -1]
    dq = deque()
    dq.append([startN-1, startM-1])
    while dq:
        curN, curM = dq.popleft()
        if curN == endN-1 and curM == endM-1:
            break
        curCost = costs[curN][curM]
        for i in range(4):
            for k in range(1, K+1):
                newN = curN + dn[i]*k
                newM = curM + dm[i]*k
                if 0>newN or newN>=N or 0>newM or newM>=M or graph[newN][newM] == '#':
                    break
                if costs[newN][newM]>curCost+1:
                    costs[newN][newM] = curCost+1
                    dq.append([newN, newM])

bfs()

print(-1 if costs[endN-1][endM-1] == sys.maxsize else costs[endN-1][endM-1])



### 정답코드
from collections import deque
import sys
input = sys.stdin.readline

# BFS
def bfs(x1, y1, x2, y2):
  queue = deque()
  # 시작점 삽입, 방문 처리
  queue.append((x1, y1))
  graph[x1][y1] = 0

  while queue:
    x, y = queue.popleft()
    # 끝점에 도착했으면 종료
    if(x == x2 and y == y2):
      return graph[x2][y2]
    # 상하좌우 탐색
    for i in range(4):
      for j in range(1, k + 1):
        nx = x + dx[i] * j
        ny = y + dy[i] * j
        # 범위 밖이면 다음 방향 탐색
        if(nx < 0 or nx >= n or ny < 0 or ny >= m): break
        # 벽이면 다음 방향 탐색
        if(graph[nx][ny] == '#'): break
        # 방문하지 않은 길이면 큐에 삽입, 방문 처리
        if(graph[nx][ny] == '.'): 
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1
        # 방문한 길인데 기준값보다 더 크다면 break하지 않고 다음 칸 이어서 탐색
        elif (graph[nx][ny] > graph[x][y]): continue
        else: break
  return -1

n, m, k = map(int, input().split())  # 세로, 가로, 1초에 이동가능한 최대 칸
# n * m (.: 빈칸 #: 벽)
graph = [list(input()) for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())  # 시작점, 끝점
visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(x1-1, y1-1, x2-1, y2-1))