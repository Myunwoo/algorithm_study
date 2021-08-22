def solution(s):
    answer=''
    s=s.lower()
    s=list(s)
    
    if s[0].isalpha():
        s[0]=s[0].upper()
    
    for i in range(len(s)-1):
        if s[i]==' ':
            if s[i+1].isalpha():
                s[i+1]=s[i+1].upper()
    
    for i in s:
        answer+=i
            
    return answer