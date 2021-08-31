#https://www.acmicpc.net/problem/1261
import sys
from collections import deque
M,N=map(int,sys.stdin.readline().split())
graph=[]
for _ in range(N):
    temp=list(sys.stdin.readline().strip())
    temp=list(map(int, temp))
    graph.append(temp)

costs=[[sys.maxsize for _ in range(M)] for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def dijk(x,y):
    global graph,costs,dx,dy
    dq=deque()
    dq.append([x,y])
    costs[x][y]=0
    while dq:
        cx,cy=dq.popleft()
        cc=costs[cx][cy]
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            #방문한 지점이 벽일 경우
            if graph[nx][ny]==1:
                #cc+1이 [nx,ny]에 도달하는 최소인 경우
                if costs[nx][ny] > cc+1:
                    costs[nx][ny]=cc+1
                    dq.append([nx,ny])
            #방문한 지점이 빈 공간일 경우
            else:
                #cc가 [nx,ny]에 도달하는 최소인 경우
                if costs[nx][ny] > cc:
                    costs[nx][ny]=cc
                    dq.append([nx,ny])

dijk(0,0)

print(costs[N-1][M-1])