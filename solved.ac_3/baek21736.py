import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().strip().split()))
graph = [list(input().strip()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

def bfs(graph, visited, i, j):
    count = 0
    dq = deque()
    dq.append([i, j])
    dn = [1, -1, 0, 0]
    dm = [0, 0, 1, -1]
    while dq:
        curN, curM = dq.popleft()
        if graph[curN][curM] == 'P':
            count += 1
        for k in range(4):
            newN = curN + dn[k]
            newM = curM + dm[k]
            if 0<=newN<N and 0<=newM<M and visited[newN][newM] == False and graph[newN][newM] != 'X':
                visited[newN][newM] = True
                dq.append([newN, newM])
    return count


count = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            visited[i][j] = True
            count = bfs(graph, visited, i, j)

print(count if count >= 1 else 'TT')