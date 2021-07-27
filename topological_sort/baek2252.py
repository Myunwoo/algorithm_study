#https://www.acmicpc.net/problem/2252
import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
degree=[0 for _ in range(N+1)]
for _ in range(M):
    A,B=map(int, sys.stdin.readline().split())
    #B가 등장하려면 A가 이전에 등장해야 하므로, B의 진입차수를 하나 늘린다.
    degree[B]+=1
    #A가 등장한 경우, A의 등장이 필요했던 학생들의 진입차수를 감소시켜, 등장할 수 있게 한다.
    graph[A].append(B)

dq=deque()
result=[]
for i in range(1,N+1):
    #진입차수가 0인 것을 dq에 삽입한다.
    if degree[i]==0:
        dq.append(i)

while dq:
    #dq에는 진입차수가 0인 것만 담겨져 있다.
    student=dq.popleft()
    #student의 등장으로 인해 진입차수가 감소해야 하는 것들의 진입 차수를 감소시킨다.
    for g in graph[student]:
        degree[g]-=1
        #진입차수가 감소되어 0이 되는 경우는 dq에 넣어준다. 
        if degree[g]==0:
            dq.append(g)
    result.append(student)

for r in result:
    print(r, end=" ")