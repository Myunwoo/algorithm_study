def calcCost(storey):
    rtn = 0
    storey = list(str(storey))
    for i in range(len(storey)-1):
        rtn += int(storey[i])

def solution(storey):
    answer = 0
    t = storey % 10
    if t <= 5:
        answer += t
        storey -= t
    else:
        answer += (10 - t)
        storey += (10 - t)
    
    if storey < 10:
        return answer
    
    print(storey)

    return answer