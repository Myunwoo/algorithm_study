#https://www.acmicpc.net/problem/11000
import sys
import heapq

N=int(sys.stdin.readline())
times=[]
for _ in range(N):
    times.append(list(map(int, sys.stdin.readline().strip().split())))
times.sort(key=lambda x:[x[0],x[1]],reverse=True)

count=1
ends=[times.pop()[1]]
while times:
    t=times.pop()
    #t의 시작시간이 가장 빠르게 끝날 수 있는 수업보다 작다면 교실이 한 개 더 필요, 끝나는 시간 저장해둠
    most_fast=heapq.heappop(ends)
    if t[0]<most_fast:
        count+=1
        heapq.heappush(ends,most_fast)
        heapq.heappush(ends,t[1])
    else:
        heapq.heappush(ends,t[1])

print(count)