#https://www.acmicpc.net/problem/1012

import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

dq = deque()

def dfs(p):
    global dq
    global field

    dq.append(p)

    while dq:
        position = dq.pop()
        curX = position[0]
        curY = position[1]
        field[curX][curY] = 0

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if nextX < 0 or nextY < 0 or nextX >= M or nextY >= N:
                continue
            if field[nextX][nextY] == 1:
                dq.append((nextX, nextY))


field = []
count = 0
counts = []

T = int(input())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    field = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().strip().split())
        field[x][y] = 1

    for i in range(M):
        for j in range(N):    
            if field[i][j] == 1:
                dfs((i, j))
                count += 1
     
    counts.append(count)
    count = 0
    field = []

for c in counts:
    print(c)