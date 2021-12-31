#https://www.acmicpc.net/problem/13913
from collections import deque
N,K=map(int, input().split())
routes=[0 for _ in range(100001)]
visited=[0 for _ in range(100001)]
dx=[-1,1,2]

if N==K:
    print(0)
    print(N)
    exit()

def bfs():
    global N,K,dx,routes,visited
    dq=deque()
    dq.append(N)
    while dq:
        curX=dq.popleft()
        if curX==K:
            print(visited[curX])
            result=[]
            while curX != N:
                result.append(curX)
                curX=routes[curX]
            result.append(N)
            result.reverse()
            for r in result:
                print(r,end=' ')
            return
                
        for i in range(len(dx)):
            if i<2:
                newX=curX+dx[i]
            else:
                newX=curX*dx[i]
            if newX<0 or newX>100000 or visited[newX]>0:
                continue
            visited[newX]=visited[curX]+1
            routes[newX]=curX
            dq.append(newX)

bfs()