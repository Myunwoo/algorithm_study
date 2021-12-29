#https://www.acmicpc.net/problem/14567
import sys
from collections import deque

N,M=map(int, sys.stdin.readline().split())
degree=[0 for _ in range(N+1)]
graph=[[] for _ in range(N+1)]
result=[0 for _ in range(N+1)]
for _ in range(M):
    a,b=map(int, sys.stdin.readline().split())
    degree[b]+=1
    graph[a].append(b)


dq=deque()
#진입 차수가 0인 것을 찾고, 찾으면 true 없으면 false리턴
def findZero():
    found=False
    for i in range(1,N+1):
        if degree[i]==0:
            degree[i]=-1
            dq.append(i)
            found=True
    return found

#dq안의 수업을 수강한 것으로 처리(후수 과목의 진입 차수를 낮춘다), 몇 학기에 들은 것인지 result에 초기화
def enroll(t):
    while dq:
        c=dq.popleft()
        result[c]=t
        for g in graph[c]:
            degree[g]-=1

time=1
while True:
    if findZero():
        enroll(time)
    else:
        break
    time+=1

for i in range(1,len(result)):
    print(result[i], end=' ')