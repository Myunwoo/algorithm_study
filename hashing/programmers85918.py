from itertools import combinations

def solution(clothes):
    answer = 1
    dic = {}
    for name, typ in clothes:
        if typ in dic:
            dic[typ] += 1
        else:
            dic[typ] = 1
    for d in dic:
        answer *= dic[d]+1
        
    return answer-1