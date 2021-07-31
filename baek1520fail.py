#https://www.acmicpc.net/problem/1520
import sys
sys.setrecursionlimit(3000)
M,N=map(int, sys.stdin.readline().split())
graph=[]
for _ in range(M):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))
visited=[[False for _ in range(N)] for _ in range(M)]
count=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(cur_x,cur_y):
    global graph,visited,count,M,N,dx,dy
    visited[cur_x][cur_y]=True
    #for v in visited:
    #    print(v)
    #print()
    if cur_x==(M-1) and cur_y==(N-1):
        count+=1
        return
    for i in range(4):
        new_x, new_y=cur_x+dx[i], cur_y+dy[i]
        #맵밖인 경우 제외
        if new_x<0 or new_y<0 or new_x>=M or new_y>=N:
            continue
        #내리막길로만 이동
        if graph[new_x][new_y] < graph[cur_x][cur_y]:
            #이전에 방문한 곳인 경우
            if visited[new_x][new_y]:
                count+=1
                return
            else:
                dfs(new_x,new_y)


dfs(0,0)
print(count)