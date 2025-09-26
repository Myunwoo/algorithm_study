import sys
from collections import deque

def bfs(graph, h, w, startH, startW):
    dq = deque()
    dq.append([startH, startW])
    graph[startH][startW] = 0

    dh = [-1, -1, -1, 0, 1, 1, 1, 0]
    dw = [-1, 0, 1, 1, 1, 0, -1, -1]

    while dq:
        curH, curW = dq.popleft()

        for i in range(8):
            newH = curH + dh[i]
            newW = curW + dw[i]
            if 0<=newH<h and 0<=newW<w and graph[newH][newW] == 1:
                graph[newH][newW] = 0
                dq.append([newH, newW])

def countIsland(graph, w, h):
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(graph, h, w, i, j)
                count += 1
    return count

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(h)]
    print(countIsland(graph, w, h))
