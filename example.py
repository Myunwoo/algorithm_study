#https://www.acmicpc.net/problem/2638

import sys

N, M = map(int, sys.stdin.readline().strip().split())

graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#녹을 예정이면 true
def checkRowCol(r, c):
    global graph
    global dx, dy
    

count = 0

def melting():
    global graph
    global count
    willMelt = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                if checkRowCol(i, j):
                    willMelt.append([i,j])
    
    if willMelt:
        for m in willMelt:
            graph[m[0]][m[1]] = 0
        count+=1
        melting()
        for i in graph:
            print(i)
        print()
    else:
        return count

print(melting())