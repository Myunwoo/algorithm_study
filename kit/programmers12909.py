def solution(s):
    answer = True
    stack = []
    
    for ss in s:
        if ss == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                answer = False
                break
    return False if stack else answer