#https://www.acmicpc.net/problem/13913
from collections import deque
N,K=map(int, input().split())
dx=[-1,1,2]

def bfs():
    global N,K,dx
    dq=deque()
    #5, 5 1, 5 1 3, 5 1 3 7 처럼 중복되는 내용의 문자열이 계속해서 dq에 저장될 수 있다. 그래서 메모리 초과가 발생하는듯?
    dq.append([N,str(N)+' ',0])
    while dq:
        curX, curRoute, curCount=dq.popleft()
        if curX==K:
            print(curCount)
            print(curRoute)
            return
        for i in range(len(dx)):
            if i<2:
                newX=curX+dx[i]
            else:
                newX=curX*dx[i]
            if newX<0 or newX>=100000:
                continue
            dq.append([newX, curRoute+str(newX)+' ', curCount+1])

bfs()