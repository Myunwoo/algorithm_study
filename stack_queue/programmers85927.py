def solution(arr):
    if not arr:
        return []
    answer = [arr[0]]
    
    for i in range(1, len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
        
    return answer