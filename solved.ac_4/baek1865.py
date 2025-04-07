import sys
import copy
from collections import deque
input = sys.stdin.readline

def bfs(graph, start):
    visited = [sys.maxsize for _ in range(N)]
    visited[start] = 0
    graph = copy.deepcopy(graph)
    dq = deque()
    dq.append((start, 0))

    while dq:
        curPos, curCost = dq.popleft()
        for i in range(len(graph[curPos])):
            if graph[curPos][i] < sys.maxsize and (graph[curPos][i] + curCost) < visited[i]:
                visited[i] = graph[curPos][i] + curCost
                dq.append((i, visited[i]))
                # 웜홀은 한 번 지나면 삭제
                if graph[curPos][i] < 0:
                    graph[curPos][i] = sys.maxsize
    return visited



TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().strip().split())
    graph = [[sys.maxsize for _ in range(N)] for _ in range(N)]
    for i in range(N):
        graph[i][i] = 0
    for _ in range(M):
        S, E, T = map(int, input().strip().split())
        m = min(graph[S-1][E-1], T)
        graph[S-1][E-1] = m
        graph[E-1][S-1] = m
    for _ in range(W):
        S, E, T = map(int, input().strip().split())
        m = min(graph[S-1][E-1], -T)
        graph[S-1][E-1] = m

    answer = 'NO'
    for i in range(N):
        if bfs(graph, i)[i] < 0:
            answer = 'YES'
            break
    print(answer)