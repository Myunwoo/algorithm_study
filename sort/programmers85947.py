def solution(d, budget):
    answer = 0
    d.sort()
    s = 0
    for dd in d:
        if s < budget:
            s += dd
            answer +=1
        else:
            break
    if s > budget:
        answer -= 1
    return answer