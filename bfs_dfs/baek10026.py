#https://www.acmicpc.net/problem/10026

import sys
from collections import deque

N = int(sys.stdin.readline().strip())

drawing = []
drawing_RG = []

for _ in range(N):
    l = list(sys.stdin.readline().strip())
    drawing.append(l)
    drawing_RG.append(l.copy())

#일반적인 합산
countR = 0
countG = 0
countB = 0

#적록색약 합산
countRG = 0
countRG_B = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque()

def dfs_normal(p):
    global drawing
    global countR
    global countG
    global countB

    #무슨 색의 덩어리를 방문처리 할 건가요?
    remember = drawing[p[0]][p[1]]
    if remember == 'R':
        countR += 1
    elif remember == 'G':
        countG += 1
    elif remember == 'B':
        countB += 1 
    dq.appendleft(p)

    while dq:
        position = dq.pop()
        curX = position[0]
        curY = position[1]

        if drawing[curX][curY] == 'V':
            continue

        drawing[curX][curY] = 'V'

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if nextX < 0 or nextY < 0 or nextX >= N or nextY >= N:
                continue

            if drawing[nextX][nextY] == remember:
                dq.appendleft((nextX, nextY))

def dfs_RG(p):
    global drawing_RG
    global countRG
    global countRG_B

    #무슨 색의 덩어리를 방문처리 할 건가요?
    remember = drawing_RG[p[0]][p[1]]
    if remember == 'R' or remember == 'G':
        countRG += 1
    elif remember == 'B':
        countRG_B += 1 

    dq.appendleft(p)

    while dq:
        position = dq.pop()
        curX = position[0]
        curY = position[1]

        if drawing_RG[curX][curY] == 'V':
            continue

        drawing_RG[curX][curY] = 'V'

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if nextX < 0 or nextY < 0 or nextX >= N or nextY >= N:
                continue

            if remember == 'R' or remember == 'G':
                if drawing_RG[nextX][nextY] == 'R' or drawing_RG[nextX][nextY] == 'G':
                    dq.appendleft((nextX, nextY))
            else:
                if drawing_RG[nextX][nextY] == remember:
                    dq.appendleft((nextX, nextY))


for i in range(N):
    for j in range(N):
        if drawing[i][j] != 'V':
            dfs_normal((i, j))

for i in range(N):
    for j in range(N):
        if drawing_RG[i][j] != 'V':
            dfs_RG((i, j))

print(countR + countG + countB, end=" ")
print(countRG + countRG_B)