def solution(n, m, section):
    answer = 0
    curstart = 0
    curEnd = 0
    for s in section:
        if s > curEnd:
            curStart = s
            curEnd = s+m-1
            answer += 1
            
    return answer