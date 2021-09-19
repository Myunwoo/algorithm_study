#https://www.acmicpc.net/problem/4796
import sys
N,M=map(int, sys.stdin.readline().split())
matrix=[]
for _ in range(N):
    matrix.append(list(map(int,sys.stdin.readline().strip())))
target=[]
for _ in range(N):
    target.append(list(map(int,sys.stdin.readline().strip())))

def convert(x,y):
    global matrix
    for i in range(x,x+3):
        for j in range(y,y+3):
            matrix[i][j]=1-matrix[i][j]

count=0
for i in range(N-2):
    for j in range(M-2):
        if matrix[i][j] != target[i][j]:
            convert(i,j)
            count+=1

can=True
for i in range(N):
    for j in range(M):
        if matrix[i][j]!=target[i][j]:
            can=False

if not can:
    print(-1)
else:
    print(count)