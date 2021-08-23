def solution(s):
    answer = True
    stack=[]
    arr=list(s)
    for a in arr:
        if a=='(':
            stack.append(a)
        elif a==')':
            if stack:
                stack.pop()
            else:
                answer=False
                break
    if stack:
        answer=False
    
    return answer