#https://www.acmicpc.net/problem/1520
import sys
sys.setrecursionlimit(10000)
M,N=map(int, sys.stdin.readline().split())
graph=[]
for _ in range(M):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))
cost=[[-1 for _ in range(N)] for _ in range(M)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(cur_x,cur_y):
    global graph,cost,M,N,dx,dy
    #도착 지점인 경우
    if cur_x==(M-1) and cur_y==(N-1):
        return 1
    
    for i in range(4):
        new_x, new_y=cur_x+dx[i], cur_y+dy[i]
        #맵밖인 경우 제외
        if new_x<0 or new_y<0 or new_x>=M or new_y>=N:
            continue
        #내리막길로만 이동
        if graph[new_x][new_y] < graph[cur_x][cur_y]:
            #이전에 방문한 곳인 경우
            if cost[new_x][new_y] != -1:
                return cost[new_x][new_y]+1
            else:
                cost[new_x][new_y]+=dfs(new_x,new_y)
                return cost[new_x][new_y]


dfs(0,0)
print(graph[0][0])