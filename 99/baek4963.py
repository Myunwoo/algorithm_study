import sys
from collections import deque

answer = []


def bfs(graph, startN, startM, N, M):

    dn = [1, 1, 1, -1, -1, -1, 0, 0]
    dm = [-1, 0, 1, -1, 0, 1, 1, -1]

    graph[startN][startM] = 0
    dq = deque()
    dq.append([startN, startM])

    while dq:
        curN, curM = dq.popleft()

        for i in range(8):
            newN = curN + dn[i]
            newM = curM + dm[i]
            if 0<=newN<N and 0<=newM<M and graph[newN][newM] == 1:
                graph[newN][newM] = 0
                dq.append([newN, newM])


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(h)]

    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                count += 1
                bfs(graph, i, j, h, w)
    answer.append(count)

for a in answer:
    print(a)