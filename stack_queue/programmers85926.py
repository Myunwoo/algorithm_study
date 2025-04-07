def solution(s):
    answer = 0
    s = list(s.split(' '))
    stack = []
    for ss in s:
        if ss == 'Z':
            if stack:
                stack.pop()
        else:
            stack.append(ss)
    if len(stack) > 0:
        answer = eval('+'.join(stack))
    return answer