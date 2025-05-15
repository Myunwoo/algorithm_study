def solution(priorities, location):
    answer = 0
    
    for i in range(len(priorities)):
        priorities[i] = [priorities[i], i]
    
    while priorities:
        val, idx = priorities[0]
        isBig = True
        for i in range(len(priorities)):
            if priorities[i][0] > val:
                priorities = priorities[i:] + priorities[:i]
                isBig = False
                break
        
        if isBig:
            answer += 1
            if priorities[0][1] == location:
                break
            priorities = priorities[1:]
    
    return answer