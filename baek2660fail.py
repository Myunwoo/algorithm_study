#https://www.acmicpc.net/problem/2660
import sys
N=int(sys.stdin.readline())
graph=[[sys.maxsize for _ in range(N)] for _ in range(N)]

while True:
    a,b=map(int, sys.stdin.readline().split())
    if a==-1 and b==-1:
        break
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j:
                graph[i][j]=0
            else:
                graph[i][j]=min(graph[i][j], graph[i][k]+graph[k][j])

results=[[] for _ in range(6)]
for i in range(len(graph)):
    m=max(graph[i])
    if m==sys.maxsize:
        continue
    results[m].append(i+1)

for i in range(len(results)):
    if results[i]:
        print(str(i)+' '+str(len(results[i])))
        for j in results[i]:
            print(j, end=' ')
        break