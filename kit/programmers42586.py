from collections import deque

def solution(progresses, speeds):
    answer = []
    idx = 0
    
    while idx < len(progresses):
        if (100 - progresses[idx]) % speeds[idx] == 0:
            count = ((100 - progresses[idx]) // speeds[idx])
        else:
            count = ((100 - progresses[idx]) // speeds[idx]) + 1
        for i in range(idx, len(progresses)):
                progresses[i] += count * speeds[i]
        
        count = 0
        while idx < len(progresses) and progresses[idx] >= 100:
            count += 1
            idx += 1
        answer.append(count)
    
    return answer