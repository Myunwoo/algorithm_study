import heapq

def solution(n, works):
    answer = 0
    for i in range(len(works)):
        works[i] = -1*works[i]
    heapq.heapify(works)
    for _ in range(n):
        if not works:
            return 0
        t = heapq.heappop(works) + 1
        if t == 0:
            continue
        else:
            heapq.heappush(works, t)
    
    if not works:
        answer = 0
    else:
        for w in works:
            answer += w**2
    return answer