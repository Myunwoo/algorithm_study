def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        newArray = array[i-1:j]
        newArray.sort()
        answer.append(newArray[k-1])
    
    return answer