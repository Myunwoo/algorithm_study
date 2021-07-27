#https://www.acmicpc.net/problem/1766
import sys
from collections import deque
from heapq import heappop,heappush

N,M=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(N+1)]
degree=[0 for _ in range(N+1)]
heap=[]

#우선순위가 뒤쳐지는 것들의 진입 차수를 늘려줌
for _ in range(M):
    A,B=map(int, sys.stdin.readline().split())
    degree[B]+=1
    heappush(graph[A],B)

#진입 차수가 0인 것들을 dq에 삽입
for i in range(1,N+1):
    if degree[i]==0:
        heappush(heap,i)

while heap:
    quiz=heappop(heap)
    for i in graph[quiz]:
        degree[i]-=1
        if degree[i]==0:
            heappush(heap,i)
    print(quiz, end=" ")