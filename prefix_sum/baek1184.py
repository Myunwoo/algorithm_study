#https://www.acmicpc.net/problem/1184
import sys
N=int(sys.stdin.readline())
graph=[]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))
prefix=[[0 for _ in range(N)] for _ in range(N)]

def rightDown(x,y):
    global graph,prefix
    arr=[]
    for i in range(x+1,N):
        for j in range(y+1,N):
            prefix[i][j]=graph[i][j]
            if i>x+1:
                prefix[i][j]+=prefix[i-1][j]
            if j>y+1:
                prefix[i][j]+=prefix[i][j-1]
            if i>x+1 and j>y+1:
                prefix[i][j]-=prefix[i-1][j-1]
            arr.append(prefix[i][j])
    return arr
                

def leftUp(x,y):
    global graph,prefix
    arr=[]
    for i in range(x,-1,-1):
        for j in range(y,-1,-1):
            prefix[i][j]=graph[i][j]
            if i<N-1:
                prefix[i][j]+=prefix[i+1][j]
            if j<N-1:
                prefix[i][j]+=prefix[i][j+1]
            if i<N-1 and j<N-1:
                prefix[i][j]-=prefix[i+1][j+1]
            arr.append(prefix[i][j])
    return arr

def leftDown(x,y):
    global graph,prefix
    arr=[]
    for i in range(x+1,N):
        for j in range(y,-1,-1):
            prefix[i][j]=graph[i][j]
            if i>x+1:
                prefix[i][j]+=prefix[i-1][j]
            if j<N-1:
                prefix[i][j]+=prefix[i][j+1]
            if i>x+1 and j<N-1:
                prefix[i][j]-=prefix[i-1][j+1]
            arr.append(prefix[i][j])
    return arr

def rightUp(x,y):
    global graph,prefix
    arr=[]
    for i in range(x,-1,-1):
        for j in range(y+1,N):
            prefix[i][j]=graph[i][j]
            if i<N-1:
                prefix[i][j]+=prefix[i+1][j]
            if j>y+1:
                prefix[i][j]+=prefix[i][j-1]
            if i<N-1 and j>y+1:
                prefix[i][j]-=prefix[i+1][j-1]
            arr.append(prefix[i][j])
    return arr
          
result=0

for i in range(N-1):
    for j in range(N-1):
        #
        ldArr=leftDown(i,j)
        ruArr=rightUp(i,j)
        for l in ldArr:
            for r in ruArr:
                if l==r:
                    result+=1
        prefix=[[0 for _ in range(N)] for _ in range(N)]


        luArr=leftUp(i,j)
        rdArr=rightDown(i,j)
        for l in luArr:
            for r in rdArr:
                if l==r:
                    result+=1
        prefix=[[0 for _ in range(N)] for _ in range(N)]

print(result)
