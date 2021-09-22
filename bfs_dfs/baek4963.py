#https://www.acmicpc.net/problem/4963
import sys
sys.setrecursionlimit(100000)
results=[]

dx=[-1,-1,-1,0,1,1,1,0]
dy=[-1,0,1,1,1,0,-1,-1]

def dfs(x,y):
    global dx,dy

    graph[x][y]=0
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1:
            dfs(nx,ny)

while True:
    w,h=map(int, sys.stdin.readline().split())
    if w==0 and h==0:
        break
    count=0
    graph=[]
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().strip().split())))
    
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                dfs(i,j)
                count+=1
    
    print(count)