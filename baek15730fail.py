#https://www.acmicpc.net/problem/15730
import sys
from collections import deque

N,M=map(int, sys.stdin.readline().split())
graph=[]
water=[[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

top=0
for i in range(N):
    for j in range(M):
        if top<graph[i][j]:
            top=graph[i][j]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(i,j,visited):
    global graph,water,dx,dy
    level=graph[i][j]
    dq=deque()
    dq.append([i,j])
    results=[]
    while dq:
        cur_x,cur_y=dq.popleft()
        visited[cur_x][cur_y]=True
        results.append([cur_x,cur_y])
        for i in range(4):
            new_x=cur_x+dx[i]
            new_y=cur_y+dy[i]
            #맵 바깥이 나오면 물이 고일 수 없음
            if new_x<0 or new_y<0 or new_x>=N or new_y>=M:
                return []
            #현재 목표보다 낮은 지형이 나오면 물이 고일 수 없음
            if graph[new_x][new_y] < level:
                return []
            #같은 높이의 지형이 나오면 탐색
            if graph[new_x][new_y]==level and not visited[new_x][new_y]:
                dq.append([new_x,new_y])
    return results


def watering(level):
    global graph
    visited=[[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            #방문한 적이 없는 목표 높이에 물채우기
            if graph[i][j]==level and not visited[i][j]:
                results=bfs(i,j,visited)
                for r in results:
                    graph[r[0]][r[1]]+=1
                    water[r[0]][r[1]]+=1

for level in range(top):
    watering(level)

s=0
for i in range(N):
    for j in range(M):
        s+=water[i][j]
print(s)