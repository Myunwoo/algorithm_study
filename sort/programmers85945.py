def solution(array, n):
    array.sort()
    answer = array[0]
    
    for i in range(1, len(array)):
        if n == array[i]:
            return n
        if i == len(array):
            return array[-1]
        
        if abs(n-answer) > abs(n-array[i]):
            answer = array[i]
    return answer