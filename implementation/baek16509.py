#https://www.acmicpc.net/problem/16509
from collections import deque
import sys

graph=[[-1 for _ in range(9)] for _ in range(10)]
moves=[
    [[0,-1],[-1,-2],[-2,-3]],
    [[0,-1],[1,-2],[2,-3]],
    [[1,0],[2,-1],[3,-2]],
    [[1,0],[2,1],[3,2]],
    [[0,1],[1,2],[2,3]],
    [[0,1],[-1,2],[-2,3]],
    [[-1,0],[-2,-1],[-3,-2]],
    [[-1,0],[-2,1],[-3,2]]
]

sang=list(map(int, input().split()))
king=list(map(int, input().split()))
graph[king[0]][king[1]]=sys.maxsize

def move(curX,curY,moveArr):
    for i in range(3):
        newX=curX+moveArr[i][0]
        newY=curY+moveArr[i][1]
        #맵 밖으로 나가는 움직임인지 확인
        if newX<0 or newY<0 or newX>=10 or newY>=9:
            return [-1,-1]
        if i<2:
            #경로상에서 왕이 길을 막고 있는지 확인
            if newX==king[0] and newY==king[1]:
                return [-1,-1]
        #도착지점에 대한 확인
        if i==2:
            #첫 방문일 때, 왕일 때만 도착지점 리턴
            if graph[newX][newY]==-1:
                return [newX,newY]
            elif graph[newX][newY]==sys.maxsize:
                return [newX,newY]
            #방문했던 점이면 [-1,-1]리턴
            else:
                return [-1,-1]


def bfs():
    global graph,sang
    dq=deque()
    dq.append(sang)
    #첫 방문처리
    graph[sang[0]][sang[1]]=0
    while dq:
        cx,cy=dq.popleft()
        #왕의 자리에 도착한 경우 스탑
        if cx==king[0] and cy==king[1]:
            print(graph[cx][cy])
            return
        #bfs를 하는 부분(상의 8가지 움직임을 지정, 상이 지나가는 자리는 move함수에서 체크)
        for i in range(8):
            nx,ny=move(cx,cy,moves[i])
            #도착 불가한 움직임이었을 경우
            if nx==-1 and ny==-1:
                continue
            #도착 가능
            else:
                dq.append([nx,ny])
                graph[nx][ny]=graph[cx][cy]+1
    print(-1)

bfs()
