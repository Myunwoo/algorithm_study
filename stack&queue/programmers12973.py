def solution(s):
    answer = -1
    temp=[]
    word=list(s)
    
    for w in word:
        temp.append(w)
        while len(temp) >= 2 and temp[len(temp)-1]==temp[len(temp)-2]:
            temp.pop()
            temp.pop()
    
    if len(temp)==0:
        answer=1
    else:
        answer=0

    return answer