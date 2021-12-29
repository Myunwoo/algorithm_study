#https://www.acmicpc.net/problem/2638
import sys
sys.setrecursionlimit(1000000)

N,M=map(int, sys.stdin.readline().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def findEx(x,y):
    global dx,dy,graph
    ex[x][y]=True
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and ex[nx][ny]==False and graph[nx][ny]==0:
            findEx(nx,ny)

def findMelt():
    global dx,dy,graph
    melting=[]
    for i in range(N):
        for j in range(M):
            if graph[i][j]>0:
                count=0
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<N and 0<=ny<M and ex[nx][ny]:
                        count+=1
                if count>=2:
                    melting.append([i,j])
    return melting

time=0
while True:
    ex=[[False for _ in range(M)] for _ in range(N)]
    findEx(0,0)

    willMelt=findMelt()
    
    if not willMelt:
        break
    
    for w in willMelt:
        graph[w[0]][w[1]]-=1
    time+=1

print(time)