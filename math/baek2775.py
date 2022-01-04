#https://www.acmicpc.net/problem/2775
import sys
T=int(sys.stdin.readline())


graph=[[0 for _ in range(15)] for _ in range(15)]
for i in range(15):
    graph[0][i]=i

for i in range(1,15):
    for j in range(1,15):
        graph[i][j]=sum(graph[i-1][:j+1])



for _ in range(T):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    print(graph[k][n])