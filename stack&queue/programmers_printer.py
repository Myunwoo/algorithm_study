from collections import deque


def solution(priorities, location):
    answer = 0
    
    dq = deque()
    for i in range(len(priorities)):
        dq.append(priorities[i])
        if i == location:
            dq.append(-1)

            
    count = 0
    
    while dq:
        printed = True
        
        now = dq.popleft()
        
        for t in dq:
            if t > now:
                dq.append(now)
                printed = False
                break
                
        if printed:
            count += 1
            if dq[0] == -1:
                answer = count
                break
        print(dq)
            
    return answer


print(solution([1,1,9,1,1,1], 0))