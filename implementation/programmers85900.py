def solution(chicken):
    answer = 0
    while chicken >= 10:
        cpn = chicken//10
        answer += chicken//10
        chicken %= 10
        chicken += cpn
    return answer