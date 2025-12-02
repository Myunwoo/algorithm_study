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

# 아래는 깔끔한 버전

def maxDistinctSubstringLengthInSessions(s: str) -> int:
    last = {}         # 문자 -> 마지막 등장 인덱스
    left = 0
    answer = 0
    
    for right, ch in enumerate(s):
        if ch == '*':
            # 세션 리셋
            last.clear()
            left = right + 1
            continue
        
        if ch in last and last[ch] >= left:
            # 현재 윈도우 안에 같은 문자가 있다면,
            # 그 문자가 있던 위치 바로 다음으로 left를 옮김
            left = last[ch] + 1
        
        last[ch] = right
        answer = max(answer, right - left + 1)
    
    return answer