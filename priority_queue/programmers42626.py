#https://programmers.co.kr/learn/courses/30/lessons/42626
from heapq import heappush,heappop,heapify

def solution(scoville, K):
    heapify(scoville)
    answer=-1
    count=0
    while scoville:
        first=heappop(scoville)
        #print('first'+str(first))
        if first>=K:
            answer=count
            break
        if len(scoville)==0:
            break
        second=heappop(scoville)
        #print('second'+str(second))
        heappush(scoville,first+second*2)
        count+=1
    return answer