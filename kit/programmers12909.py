def solution(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:
            if count > 0:
                count -= 1
            else:
                return False
    
    return False if count > 0 else True