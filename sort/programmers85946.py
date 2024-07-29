def solution(emergency):
    answer = []
    emergency_s = sorted(emergency, reverse=True)
    for e in emergency:
        answer.append(emergency_s.index(e)+1)
    
    return answer