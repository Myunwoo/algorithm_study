def solution(arr):
    answer = [arr[0]]
    
    # arr
    # answer.append(arr[i]) <- answer[-1] <> arr[i]
    # O(n)
    
    # arr.append() 1백만 건
    # arr resizing
    
    for i in range(1, len(arr)):
        if arr[i] == answer[-1]:
            continue
        answer.append(arr[i])
    
    return answer