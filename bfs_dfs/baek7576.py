import sys
from collections import deque

#m은 가로, 은 n은 세로
m, n = map(int, input().split())

basket = []

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

dq = deque()

#토마토 상자 입력, 익은 토마토 위치를 deque에 저장
for i in range(n):
    basket.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if basket[i][j] == 1:
            dq.append((i,j))

#일자를 구분하기 위한 요소 삽입
dq.append((-100,-100))

def bfs(dq):
    day = -1
    while True:
        if len(dq) == 0:
            break

        position = dq.popleft()
        curR = position[0]
        curC = position[1]

        if curR == -100 and curC == -100:
            day += 1
            if len(dq) > 0:
                dq.append((-100,-100))
            continue

        for i in range(4):
            newR = curR + dr[i]
            newC = curC + dc[i]

            if newR < 0 or newR >= n or newC < 0 or newC >= m:
                continue
            if basket[newR][newC] == -1:
                continue
            if basket[newR][newC] == 1:
                continue
            basket[newR][newC] = 1
            dq.append((newR,newC))

    full = True

    for i in range(n):
        for j in range(m):
            if basket[i][j] == 0:
                full = False
                break
    
    if full == True:
        print(day)
    else:
        print(-1)

bfs(dq)