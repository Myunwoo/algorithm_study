def solution(array):
    answer = []
    m = -1
    mi = -1
    for i in range(len(array)):
        if array[i] > m:
            m = array[i]
            mi = i
    answer = [m, mi]
    return answer