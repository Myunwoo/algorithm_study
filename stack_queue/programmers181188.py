def solution(targets):
    answer = 0
    targets.sort(key=lambda x:[x[1], x[0]])
    curStart, curEnd = 0, 0
    
    for newStart, newEnd in targets:
        if newStart >= curEnd:
            answer += 1
            curStart, curEnd = newStart, newEnd
    return answer