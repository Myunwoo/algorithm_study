#https://www.acmicpc.net/problem/17265
import sys
from collections import deque

N=int(sys.stdin.readline())
graph=[]
for _ in range(N):
    graph.append(list(sys.stdin.readline().strip().split()))

results=[[[sys.maxsize,-sys.maxsize] for _ in range(N)] for _ in range(N)]
results[0][0]=[graph[0][0],graph[0][0]]
dx=[0,1]
dy=[1,0]

def bfs():
    global graph,results,dx,dy
    dq=deque()
    dq.append([0,0,graph[0][0],''])
    while dq:
        cx,cy,lcost,coperand=dq.popleft()
        for i in range(2):
            nx=cx+dx[i]
            ny=cy+dy[i]
        if nx<0 or ny<0 or nx>=N or ny>=N:
            continue
        if graph[nx][ny].isdigit():
            results[nx][ny][0]=min(results[nx][ny][0], eval(graph[nx][ny]+coperand+lcost))
            results[nx][ny][1]=max(results[nx][ny][1], eval(graph[nx][ny]+coperand+lcost))
            dq.append([nx,ny,graph[nx][ny],''])
        else:
            results[nx][ny][0]=min(results[nx][ny][0],int(graph[cx][cy]))
            results[nx][ny][1]=max(results[nx][ny][1],int(graph[cx][cy]))
            dq.append([nx,ny,lcost,graph[nx][ny]])

bfs()
for r in results:
    print(r)