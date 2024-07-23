def solution(s):
    stack = []
    for ss in s:
        if ss == '(':
            stack.append(ss)
        elif ss == ')':
            if not stack or stack[-1] != '(':
                return False
            else:
                stack.pop()
    return not stack