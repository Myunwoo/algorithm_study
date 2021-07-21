#https://www.acmicpc.net/problem/9376
import sys
from collections import deque

dh=[1,-1,0,0]
dw=[0,0,1,-1]

def bfs(graph, h, w, x, y):
    global dh,dw
    costs=[[-1 for _ in range(w+2)] for _ in range(h+2)]
    #시점은 벽이 아님이 보장됨
    dq=deque()
    dq.append([x,y])
    costs[x][y]=0

    while dq:
        ph,pw=dq.popleft()
        p_cost=costs[ph][pw]
        for i in range(4):
            nh=ph+dh[i]
            nw=pw+dw[i]
            #맵을 넘어가는 경우, 벽인 경우 제외
            if nh<0 or nw<0 or nh>=(h+2) or nw>=(w+2) or graph[nh][nw]=='*':
                continue
            if costs[nh][nw]!=-1:
                continue
            #문인 경우, 이전 탐색 칸의 비용+1을 대입
            if graph[nh][nw]=='#':
                costs[nh][nw]=p_cost+1
                dq.append([nh,nw])
            #빈 공간인 경우, 이전 탐색 칸의 비용을 대입
            else:
                costs[nh][nw]=p_cost
                dq.appendleft([nh,nw])
    return costs

t=int(sys.stdin.readline())
results=[]
for _ in range(t):
    graph=[]
    h, w = map(int, sys.stdin.readline().split())
    graph.append([])
    for _ in range(w+2):
        graph[0].append('.')
    for _ in range(h):
        graph.append(['.']+list(sys.stdin.readline().strip())+['.'])
    graph.append([])
    for _ in range(w+2):
        graph[h+1].append('.')
    
    r0=bfs(graph,h,w,0,0)
    pos=[]
    for i in range(h+2):
        for j in range(w+2):
            if graph[i][j]=='$':
                pos.append([i,j])
    r1=bfs(graph,h,w,pos[0][0],pos[0][1])
    r2=bfs(graph,h,w,pos[1][0],pos[1][1])

    m=sys.maxsize
    for i in range(h+2):
        for j in range(w+2):
            if graph[i][j]=='*':
                continue
            if r0[i][j]==-1 or r1[i][j]==-1 or r2[i][j]==-1:
                continue
            total_cost=r0[i][j]+r1[i][j]+r2[i][j]
            if graph[i][j]=='#':
                total_cost-=2
            m=min(m,total_cost)
    results.append(m)

for r in results:
    print(r)