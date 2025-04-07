def solution(array):
    answer = 0
    for a in array:
        for i in str(a):
            if i == '7':
                answer += 1
    return answer