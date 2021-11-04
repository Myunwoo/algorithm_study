#https://www.acmicpc.net/problem/2109
import sys,heapq
n=int(sys.stdin.readline())

courses=[]
for _ in range(n):
    courses.append(list(map(int, sys.stdin.readline().strip().split())))

#가장 비싼 수업부터 할 것임.
courses.sort(key=lambda x:x[1])
result=0
heap=[]

for course in courses:
    #수업을 heap에 삽입
    heapq.heappush(heap,course[0])
    #하루에 한 개의 수업을 하는데, 이때 이미 수업을 했을 날이 기한인 강의가 입력으로 들어오면
    #수업료가 가장 적은 수업을 삭제한다.
    if course[1] < len(heap):
        heapq.heappop(heap)


print(sum(heap))