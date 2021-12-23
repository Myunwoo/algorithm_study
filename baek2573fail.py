#https://www.acmicpc.net/problem/2573
import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())
graph=[]
visited=[[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
year=0

#모든 땅을 찾아서 자신이 얼마만큼 녹아야 하는지 파악
def countMelt():
    global graph,N,M,dx,dy,year
    dic={}
    for i in range(N):
        for j in range(M):
            if graph[i][j]>0:
                meltCount=0
                for k in range(4):
                    if graph[i+dx[k]][j+dy[k]]==0:
                        meltCount+=1
                if meltCount>0:
                    if (i,j) in dic:
                        dic[(i,j)]+=meltCount
                    else:
                        dic[(i,j)]=meltCount
    for d in dic:
        x,y=d
        graph[x][y]-=dic[d]
    year+=1

#땅을 bfs해서 땅이 몇개의 덩어리인지 파악
def groundBfs():
    global graph,N,M,dx,dy,year,visited
    dq=deque()
    count=0
    for i in range(N):
        for j in range(M):
            if graph[i][j]>0 and not visited[i][j]:
                dq.append([i,j])
                count+=1
            while dq:
                cx,cy=dq.popleft()
                visited[cx][cy]=True
                for k in range(4):
                    nx=cx+dx[k]
                    ny=cy+dy[k]
                    if graph[nx][ny]>0 and not visited[nx][ny]:
                        dq.append([nx,ny])
    visited=[[False for _ in range(M)] for _ in range(N)]
    return count

def solve():
    r=0
    while True:
        r=groundBfs()
        if r==0:
            print(0)
            return
        elif r==1:
            countMelt()
        else:
            print(year)
            return

solve()