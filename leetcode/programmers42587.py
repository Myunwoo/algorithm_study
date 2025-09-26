from collections import deque
from heapq import heappop, heappush, heapify

def solution(priorities, location):
    answer = 0
    
    priorities = [[-el, idx] for idx, el in enumerate(priorities)]
    dq = deque(priorities)
    heapify(priorities)
    
    
    while priorities:
        foundAnswer = False
        
        # 현재 실행되어야 할 우선순위
        targetP, targetIdx = heappop(priorities)
        
        while dq:
            curP, curIdx = dq.popleft()
            if curP == targetP:
                answer += 1
                if curIdx == location:
                    foundAnswer = True
                break
            else:
                dq.append([curP, curIdx])

        if foundAnswer:
            break
    return answer