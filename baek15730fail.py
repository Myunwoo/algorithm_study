#https://www.acmicpc.net/problem/15730
import sys
from collections import deque

N,M=map(int, sys.stdin.readline().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

count=0
def bfs(x,y,l):
    global N,M,graph,count,dx,dy
    visited=[[False for _ in range(M)] for _ in range(N)]
    dq=deque()
    dq.append([x,y])
    while dq:
        cx,cy=dq.popleft()
        visited[cx][cy]=True
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            #x,y가 맵의 가장자리인 경우 물 못채움
            if nx<0 or ny<0 or nx>=N or ny>=M:
                return
                #방문한 적이 없는 칸 중
            if not visited[nx][ny]:
                #목표와 같은 높이의 칸이 인접해 있다면 전이
                if graph[nx][ny]==l:
                    dq.append([nx,ny])
                #목표보다 낮은 칸이 인접해 있다면 물을 채울 수 없음
                elif graph[nx][ny]<l:
                    return
    #주변이 자신보다 높고, 가장자리에 위치하지 않은 칸들의 목록이 target에 저장됨.
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                graph[i][j]+=1
                count+=1


level=0
#0부터 10000까지 돌며 물을 채울 것
while level<10001:
    for i in range(N):
        for j in range(M):
            #현재 물을 채워야 할 칸에 대하여 bfs를 수행
            if graph[i][j]==level:
                bfs(i,j,level)
    level+=1

print(count)