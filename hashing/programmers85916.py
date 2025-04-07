def solution(participant, completion):
    answer = ''
    dic = {}
    for c in completion:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    
    for p in participant:
        if p in dic and dic[p] > 0:
            dic[p] -= 1
        elif p in dic and dic[p] == 0:
            answer = p
            break
        elif p not in dic:
            answer = p
            break
    return answer