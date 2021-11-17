#https://www.acmicpc.net/problem/17129
import sys
from collections import deque
n,m=map(int, sys.stdin.readline().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
distance=[[0 for _ in range(m)] for _ in range(n)]
dq=deque()

def bfs(i,j):
    dq.append([i,j])
    distance[i][j]=1
    while dq:
        cx,cy=dq.popleft()
        for k in range(4):
            nx=cx+dx[k]
            ny=cy+dy[k]
            #맵 밖이거나 벽일 때
            if nx<0 or ny<0 or nx>=n or ny>=m or graph[nx][ny]==1:
                continue
            #너비우선 탐색이므로 방문하지 않은 경우가 최단거리 방문임
            if distance[nx][ny]==0:
                distance[nx][ny]=distance[cx][cy]+1
                dq.append([nx,ny])
                if graph[nx][ny] in [3,4,5]:
                    print('TAK')
                    #시작을 1로 했기 때문에 1 빼줌
                    print(distance[nx][ny]-1)
                    exit()
    


for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            bfs(i,j)

print('NIE')