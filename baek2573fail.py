#https://www.acmicpc.net/problem/2573
import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
year=0

#전달받은 점이 몇 회 녹아야 하는지 계산하는 함수
def countMelt(mq,cx,cy):
    global graph,N,M,dx,dy
    count=0
    for i in range(4):
        nx=cx+dx[i]
        ny=cy+dy[i]
        if graph[nx][ny]==0:
            count+=1
    if count>0:
        mq.append([cx,cy,count])

#땅을 bfs해서 땅이 몇개의 덩어리인지 파악
def groundBfs(visited):
    global graph,N,M,dx,dy,year
    dq=deque()
    count=0
    mq=deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j]>0 and not visited[i][j]:
                dq.append([i,j])
                count+=1
                while dq:
                    cx,cy=dq.popleft()
                    countMelt(mq,cx,cy)
                    visited[cx][cy]=True
                    for k in range(4):
                        nx=cx+dx[k]
                        ny=cy+dy[k]
                        if graph[nx][ny]>0 and not visited[nx][ny]:
                            dq.append([nx,ny])
    
    for m in mq:
        graph[m[0]][m[1]]-=m[2]
        if graph[m[0]][m[1]]<0:
            graph[m[0]][m[1]]=0
    return count

def solve():
    global year
    r=0
    while True:
        visited=[[False for _ in range(M)] for _ in range(N)]
        r=groundBfs(visited)
        if r==0:
            print(0)
            return
        elif r==1:
            year+=1
        else:
            print(year)
            return

solve()