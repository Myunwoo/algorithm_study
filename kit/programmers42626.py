from heapq import heapify, heappop, heappush

def solution(scoville, K):
    heapify(scoville)
    answer = 0
    
    while len(scoville) > 1:
        first = heappop(scoville)
        if first >= K:
            break
        second = heappop(scoville)
        
        heappush(scoville, first + second*2)
        answer += 1
    
    if heappop(scoville) < K:
        answer = -1
    
    return answer