def solution(routes):
    answer = 0
    cur = -30001
    routes.sort(key=lambda x:[x[1], x[0]])
    
    for i in range(len(routes)):
        start, end = routes[i]
        if start > cur:
            cur = end
            answer += 1
            
    return answer
    