def solution(clothes):
    answer = 1
    dic = dict()
    
    for c in clothes:
        val, typ = c
        if typ in dic:
            dic[typ] += 1
        else:
            dic[typ] = 1
    
    arr = dic.values()
    
    for a in arr:
        answer *= (a + 1)
    
    return answer - 1