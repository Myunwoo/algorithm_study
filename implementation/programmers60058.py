def isGood(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return False
    return not stack

def getUV(p):
    if p == '':
        return ''
    rightCount = 0
    leftCount = 0
    u = ''
    v = ''
    for i in range(len(p)):
        if p[i] == '(':
            rightCount += 1
        elif p[i] == ')':
            leftCount += 1
        if rightCount == leftCount:
            u = p[:leftCount+rightCount]
            v = p[leftCount+rightCount:]
            break
    if isGood(u):
        u += getUV(v)
    else:
        temp = '(' + getUV(v) +')'
        for i in range(1, len(u)-1):
            if u[i] == '(':
                temp += ')'
            else:
                temp += '('
        return temp
    return u

def solution(p):
    answer = ''
    if p == '':
        return answer
    answer = getUV(p)
    
    return answer