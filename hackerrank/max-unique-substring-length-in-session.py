def maxDistinctSubstringLengthInSessions(sessionString):
    dic = {}
    left, right = 0, 0
    answer = 0
    
    while left <= right < len(sessionString):
        rv = sessionString[right]
        
        if rv == '*':
            right += 1
            left = right
            dic = {}
            continue
        
        if rv not in dic:
            dic[rv] = True
            answer = max(answer, right - left + 1)
            right += 1
            continue
        
        if rv in dic:
            while True:
                lv = sessionString[left]
                if lv == rv:
                    break
                del dic[lv]
                left += 1
            right += 1
            left += 1
    
    return answer

