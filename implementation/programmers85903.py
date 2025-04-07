def solution(cards1, cards2, goal):
    answer = 'Yes'
    cards1 = cards1[::-1]
    cards2 = cards2[::-1]
    goal = goal[::-1]
    
    while goal:
        cur = goal.pop()
        if cards1 and cards1[-1] == cur:
            cards1.pop()
        elif cards2 and cards2[-1] == cur:
            cards2.pop()
        else:
            answer = 'No'
            break
    return answer