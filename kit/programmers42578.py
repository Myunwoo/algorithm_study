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

def solution(clothes):
    hashMap = {}
    answer = 1
    
    for name, kind in clothes:
        if kind in hashMap:
            hashMap[kind] += 1
        else:
            hashMap[kind] = 1

    for key in hashMap:
        answer *= hashMap[key] + 1
    
    return answer - 1