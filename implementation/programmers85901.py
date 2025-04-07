def solution(i, j, k):
    k = str(k)
    answer = 0
    for val in range(i,j+1):
        for v in list(str(val)):
            if v == k:
                answer += 1
    return answer