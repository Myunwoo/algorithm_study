#https://www.acmicpc.net/problem/21278
import sys
N,M=map(int, sys.stdin.readline().split())
graph=[[sys.maxsize for _ in range(N)] for _ in range(N)]
for _ in range(M):
    A,B=map(int, sys.stdin.readline().split())
    graph[A-1][B-1]=1
    graph[B-1][A-1]=1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j:
                graph[i][j]=0
            else:
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

m=sys.maxsize
chicken1=-1
chicken2=-1
#치킨가게를 두 가지 뽑음
for i in range(N-1):
    for j in range(i+1,N):
        s=0
        #k 로부터 치킨집(i,j)까지의 거리 중 최소인 녀석을 합계에 더함
        for k in range(N):
            s+=min(graph[k][i],graph[k][j])
        if m>s:
            m=s
            chicken1=i
            chicken2=j

print(chicken1+1, chicken2+1,m)