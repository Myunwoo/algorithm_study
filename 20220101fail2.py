#https://www.acmicpc.net/problem/13913
from collections import deque
N,K=map(int, input().split())
routes=[0 for _ in range(100001)]
dx=[-1,1,2]

def bfs():
    global N,K,dx
    dq=deque()
    #5, 5 1, 5 1 3, 5 1 3 7 처럼 중복되는 내용의 문자열이 계속해서 dq에 저장될 수 있다. 그래서 메모리 초과가 발생하는듯?
    dq.append(N)
    while dq:
        curX=dq.popleft()
        if curX==K:
            return
        for i in range(len(dx)):
            if i<2:
                newX=curX+dx[i]
            else:
                newX=curX*dx[i]
            if newX<0 or newX>=100000 or routes[newX]>-1 or newX==N:
                continue
            routes[newX]=curX
            dq.append(newX)

bfs()

#경로 배열은 전역에 result로 존재하는데 어째서 메모리 초과...?
result=[]
def findPath(k):
    global routes,result
    if routes[k]==-1:
        return
    result.append(routes[k])
    findPath(routes[k])

findPath(K)

print(len(result)+1)
for i in range(len(result)-1,-1,-1):
    print(result[i],end=' ')
print(K)