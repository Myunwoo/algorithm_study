def solution(order):
    answer = 0
    order = str(order)
    for o in order:
        if o in ['3', '6', '9']:
            answer += 1
    return answer