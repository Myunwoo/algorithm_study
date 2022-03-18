#https://programmers.co.kr/learn/courses/30/lessons/42626
from heapq import heappush,heappop,heapify

def solution(scoville, K):
    heapify(scoville)
    answer=0
    
    while len(scoville)>1:
        if scoville[0]>=K:
            break
        f1=heappop(scoville)
        f2=heappop(scoville)
        new=f1+f2*2
        heappush(scoville,new)
        answer+=1
    
    if scoville[0]<K:
        answer=-1
    return answer